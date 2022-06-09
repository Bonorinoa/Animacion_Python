from typing import Dict, Tuple, Union

from .buffer import Buffer
from .renderbuffer import Renderbuffer
from .texture import Texture

__all__ = ['Framebuffer']


class Framebuffer:
    '''
        A :py:class:`Framebuffer` is a collection of buffers that can be used as the destination for rendering.
        The buffers for Framebuffer objects reference images from either Textures or Renderbuffers.

        Create a :py:class:`Framebuffer` using :py:meth:`Context.framebuffer`.
    '''

    __slots__ = ['mglo', '_color_attachments', '_depth_attachment', '_size', '_samples', '_glo', 'ctx', 'extra']

    def __init__(self):
        self.mglo = None  #: Internal representation for debug purposes only.
        self._color_attachments = None
        self._depth_attachment = None
        self._size = (None, None)
        self._samples = None
        self._glo = None
        self.ctx = None  #: The context this object belongs to
        self.extra = None  #: Any - Attribute for storing user defined objects
        raise TypeError()

    def __repr__(self):
        return '<Framebuffer: %d>' % self.glo

    def __eq__(self, other):
        return type(self) is type(other) and self.mglo is other.mglo

    def __hash__(self) -> int:
        return id(self)

    @property
    def viewport(self) -> Tuple[int, int, int, int]:
        '''
            tuple: Get or set the viewport of the framebuffer.
        '''

        return self.mglo.viewport

    @viewport.setter
    def viewport(self, value):
        self.mglo.viewport = tuple(value)

    @property
    def scissor(self) -> Tuple[int, int, int, int]:
        '''
            tuple: Get or set the scissor box of the framebuffer.

            When scissor testing is enabled fragments outside
            the defined scissor box will be discarded. This
            applies to rendered geometry or :py:meth:`Framebuffer.clear`.

            Setting is value enables scissor testing in the framebuffer.
            Setting the scissor to ``None`` disables scissor testing
            and reverts the scissor box to match the framebuffer size.

            Example::

                # Enable scissor testing
                >>> ctx.scissor = 100, 100, 200, 100
                # Disable scissor testing
                >>> ctx.scissor = None
        '''

        return self.mglo.scissor

    @scissor.setter
    def scissor(self, value):
        if value is None:
            self.mglo.scissor = None
        else:
            self.mglo.scissor = tuple(value)

    @property
    def color_mask(self) -> Tuple[bool, bool, bool, bool]:
        '''tuple: The color mask of the framebuffer.

        Color masking controls what components in color attachments will be
        affected by fragment write operations.
        This includes rendering geometry and clearing the framebuffer.

        Default value: ``(True, True, True, True)``.

        Examples::

            # Block writing to all color components (rgba) in color attachments
            fbo.color_mask = False, False, False, False

            # Re-enable writing to color attachments
            fbo.color_mask = True, True, True, True

            # Block fragment writes to alpha channel
            fbo.color_mask = True, True, True, False
        '''

        return self.mglo.color_mask

    @color_mask.setter
    def color_mask(self, value):
        self.mglo.color_mask = value

    @property
    def depth_mask(self) -> bool:
        '''bool: The depth mask of the framebuffer.

        Depth mask enables or disables write operations to the depth buffer.
        This also applies when clearing the framebuffer.
        If depth testing is enabled fragments will still be culled, but
        the depth buffer will not be updated with new values. This is
        a very useful tool in many rendering techniques.

        Default value: ``True``
        '''

        return self.mglo.depth_mask

    @depth_mask.setter
    def depth_mask(self, value):
        self.mglo.depth_mask = value

    @property
    def width(self) -> int:
        '''
            int: The width of the framebuffer.

            Framebuffers created by a window will only report its initial size.
            It's better get size information from the window itself.
        '''

        return self._size[0]

    @property
    def height(self) -> int:
        '''
            int: The height of the framebuffer.

            Framebuffers created by a window will only report its initial size.
            It's better get size information from the window itself.
        '''

        return self._size[1]

    @property
    def size(self) -> tuple:
        '''
            tuple: The size of the framebuffer.

            Framebuffers created by a window will only report its initial size.
            It's better get size information from the window itself.
        '''

        return self._size

    @property
    def samples(self) -> int:
        '''
            int: The samples of the framebuffer.
        '''

        return self._samples

    @property
    def bits(self) -> Dict[str, str]:
        '''
            dict: The bits of the framebuffer.
        '''

        return self.mglo.bits

    @property
    def color_attachments(self) -> Tuple[Union[Texture, Renderbuffer], ...]:
        '''
            tuple: The color attachments of the framebuffer.
        '''

        return self._color_attachments

    @property
    def depth_attachment(self) -> Union[Texture, Renderbuffer]:
        '''
            Texture or Renderbuffer: The depth attachment of the framebuffer.
        '''

        return self._depth_attachment

    @property
    def glo(self) -> int:
        '''
            int: The internal OpenGL object.
            This values is provided for debug purposes only.
        '''

        return self._glo

    def clear(self, red=0.0, green=0.0, blue=0.0, alpha=0.0, depth=1.0, *, viewport=None, color=None) -> None:
        '''
            Clear the framebuffer.

            If a `viewport` passed in, a scissor test will be used to clear the given viewport.
            This viewport take prescense over the framebuffers :py:attr:`~moderngl.Framebuffer.scissor`.
            Clearing can still be done with scissor if no viewport is passed in.

            This method also respects the
            :py:attr:`~moderngl.Framebuffer.color_mask` and
            :py:attr:`~moderngl.Framebuffer.depth_mask`. It can for example be used to only clear
            the depth or color buffer or specific components in the color buffer.

            If the `viewport` is a 2-tuple it will clear the
            ``(0, 0, width, height)`` where ``(width, height)`` is the 2-tuple.

            If the `viewport` is a 4-tuple it will clear the given viewport.

            Args:
                red (float): color component.
                green (float): color component.
                blue (float): color component.
                alpha (float): alpha component.
                depth (float): depth value.

            Keyword Args:
                viewport (tuple): The viewport.
                color (tuple): Optional tuple replacing the red, green, blue and alpha arguments
        '''

        if color is not None:
            red, green, blue, alpha, *_ = tuple(color) + (0.0, 0.0, 0.0, 0.0)

        if viewport is not None:
            viewport = tuple(viewport)

        self.mglo.clear(red, green, blue, alpha, depth, viewport)

    def use(self) -> None:
        '''
            Bind the framebuffer. Sets the target for rendering commands.
        '''

        self.ctx.fbo = self
        self.mglo.use()

    def read(self, viewport=None, components=3, *, attachment=0, alignment=1, dtype='f1') -> bytes:
        '''
            Read the content of the framebuffer.

            Args:
                viewport (tuple): The viewport.
                components (int): The number of components to read.

            Keyword Args:
                attachment (int): The color attachment.
                alignment (int): The byte alignment of the pixels.
                dtype (str): Data type.

            Returns:
                bytes
        '''

        return self.mglo.read(viewport, components, attachment, alignment, dtype)

    def read_into(self, buffer, viewport=None, components=3, *,
                  attachment=0, alignment=1, dtype='f1', write_offset=0) -> None:
        '''
            Read the content of the framebuffer into a buffer.

            Args:
                buffer (bytearray): The buffer that will receive the pixels.
                viewport (tuple): The viewport.
                components (int): The number of components to read.

            Keyword Args:
                attachment (int): The color attachment.
                alignment (int): The byte alignment of the pixels.
                dtype (str): Data type.
                write_offset (int): The write offset.
        '''

        if type(buffer) is Buffer:
            buffer = buffer.mglo

        return self.mglo.read_into(buffer, viewport, components, attachment, alignment, dtype, write_offset)

    def release(self) -> None:
        '''
            Release the ModernGL object.
        '''

        self.mglo.release()
