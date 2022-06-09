__all__ = ['Scope']


class Scope:
    '''
        This class represents a Scope object.

        Responsibilities on enter:

        - Set the enable flags.
        - Bind the framebuffer.
        - Assigning textures to texture locations.
        - Assigning buffers to uniform buffers.
        - Assigning buffers to shader storage buffers.

        Responsibilities on exit:

        - Restore the enable flags.
        - Restore the framebuffer.
    '''

    __slots__ = ['mglo', 'ctx', 'extra']

    def __init__(self):
        self.mglo = None  #: Internal representation for debug purposes only.
        self.ctx = None  #: The context this object belongs to
        self.extra = None  #: Any - Attribute for storing user defined objects
        raise TypeError()

    def __repr__(self):
        return '<Scope>'

    def __hash__(self) -> int:
        return id(self)

    def __enter__(self):
        self.mglo.begin()
        return self

    def __exit__(self, *args):
        self.mglo.end()
