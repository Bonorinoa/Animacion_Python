from manim import *

class CodeFromString(Scene):
    def construct(self):
        code = '''from manim import *
from manim.opengl import *

class OpenGLIntro(Scene):
    def construct(self):
        hello_world = Tex("Hello World!").scale(3)
        self.play(Write(hello_world))
        self.play(
            self.camera.animate.set_euler_angles(
                theta=-10*DEGREES,
                phi=50*DEGREES
            )
        )
        self.play(FadeOut(hello_world))
        surface = OpenGLSurface(
            lambda u, v: (u, v, u*np.sin(v) + v*np.cos(u)),
            u_range=(-3, 3),
            v_range=(-3, 3)
        )
        surface_mesh = OpenGLSurfaceMesh(surface)
        self.play(Create(surface_mesh))
        self.play(FadeTransform(surface_mesh, surface))
        self.wait()
        light = self.camera.light_source
        self.play(light.animate.shift([0, 0, -20]))
        self.play(light.animate.shift([0, 0, 10]))
        self.play(self.camera.animate.set_euler_angles(theta=60*DEGREES))
        
        self.interactive_embed()
'''
        rendered_code = Code(code=code, tab_width=3, background="window",
                            language="Python", line_spacing=0.5, style="dracula", font="Monospace")
        self.add(rendered_code.scale(0.67))


class lambdaFunc(Scene):
    def construct(self):

        titulo = Title("Destilando funciones lambda")

        ejemplo = Tex(r"lambda ", r" $x$ ", r" : ", r" $x + 4$")

        box1 = SurroundingRectangle(ejemplo[0], buff=0.2)
        box2 = SurroundingRectangle(ejemplo[1], buff=0.2)
        box3 = SurroundingRectangle(ejemplo[2], buff=0.2)
        box4 = SurroundingRectangle(ejemplo[3], buff=0.2)

        texto1 = Text("Operador", font_size=22, color=RED).next_to(box1, UL).shift(UP)
        texto2 = Text("Variable(s)", font_size=22, color=BLUE).next_to(box2, DOWN).shift(DOWN)
        texto3 = Text("Indentador de Python", font_size=22, color=WHITE).next_to(box3, UP).shift(UP)
        texto4 = Text("Operación", font_size=22, color=GREEN_B).next_to(box4, UR).shift(UP)

        arrow1 = Arrow(start=[box1.get_x(), box1.get_y()+0.5, 0],
                        end=[texto1.get_x(), texto1.get_y()-0.2, 0],
                        color=RED, buff=0.2)

        arrow2 = Arrow(start=[box2.get_x(), box2.get_y()-0.5, 0],
                        end=[texto2.get_x(), texto2.get_y()+0.2, 0],
                        color=BLUE, buff=0.2)

        arrow3 = Arrow(start=[box3.get_x(), box3.get_y()+0.5, 0],
                        end=[texto3.get_x(), texto3.get_y()-0.2, 0],
                        color=WHITE, buff=0.2)

        arrow4 = Arrow(start=[box4.get_x(), box4.get_y()+0.5, 0],
                        end=[texto4.get_x(), texto4.get_y()-0.2, 0],
                        color=GREEN_B, buff=0.2)

        self.play(Write(ejemplo))
        
        group1 = VGroup(box1, texto1, arrow1)

        group2 = VGroup(box2, texto2, arrow2)
        group3 = VGroup(box3, texto3, arrow3)
        group4 = VGroup(box4, texto4, arrow4)

        self.wait(5)

        self.play(Create(group1))

        self.wait(5)

        self.play(ReplacementTransform(group1, group2))

        self.wait(5)
        
        self.play(ReplacementTransform(group2, group3))

        self.wait(5)
        
        self.play(ReplacementTransform(group3, group4))

        self.wait(5)

        self.play(Uncreate(group4))

        self.play(ejemplo.animate.shift(UP), FadeIn(Tex(r"=")))

        self.wait()

        ejemploDef = Tex(r"\textbf{def} nombreFunc($x$): \\ \hspace{1.5em} \textbf{return} $x + 4$").shift(DOWN)

        self.play(Create(ejemploDef))

        self.wait(5)

        self.clear()

        # ejemplo2
        ejemplo2 = Tex(r"lambda ", r" $x,y$ ", r" : ", r" ($x^2 + y^2 - 1)^3 - x^2 \cdot y^3$ ")

        box1b = SurroundingRectangle(ejemplo2[0], buff=0.2)
        box2b = SurroundingRectangle(ejemplo2[1], buff=0.2)
        box3b = SurroundingRectangle(ejemplo2[2], buff=0.2)
        box4b = SurroundingRectangle(ejemplo2[3], buff=0.2)

        texto1b = Text("Operador", font_size=22, color=RED).next_to(box1b, UL).shift(UP)
        texto2b = Text("Variable(s)", font_size=22, color=BLUE).next_to(box2b, DOWN).shift(DOWN)
        texto3b = Text("Indentador de Python", font_size=22, color=WHITE).next_to(box3b, UP).shift(UP)
        texto4b = Text("Operación", font_size=22, color=GREEN_B).next_to(box4b, UR).shift(UP)

        arrow1b = Arrow(start=[box1b.get_x(), box1b.get_y()+0.5, 0],
                        end=[texto1b.get_x(), texto1b.get_y()-0.2, 0],
                        color=RED, buff=0.2)

        arrow2b = Arrow(start=[box2b.get_x(), box2b.get_y()-0.5, 0],
                        end=[texto2b.get_x(), texto2b.get_y()+0.2, 0],
                        color=BLUE, buff=0.2)

        arrow3b = Arrow(start=[box3b.get_x(), box3b.get_y()+0.5, 0],
                        end=[texto3b.get_x(), texto3b.get_y()-0.2, 0],
                        color=WHITE, buff=0.2)

        arrow4b = Arrow(start=[box4b.get_x(), box4b.get_y()+0.5, 0],
                        end=[texto4b.get_x(), texto4b.get_y()-0.2, 0],
                        color=GREEN_B, buff=0.2)

        self.play(Write(ejemplo2))
        
        group1b = VGroup(box1b, texto1b, arrow1b)

        group2b = VGroup(box2b, texto2b, arrow2b)
        group3b = VGroup(box3b, texto3b, arrow3b)
        group4b = VGroup(box4b, texto4b, arrow4b)

        self.wait(5)

        self.play(Create(group1b))

        self.wait(5)

        self.play(ReplacementTransform(group1b, group2b))

        self.wait(5)
        
        self.play(ReplacementTransform(group2b, group3b))

        self.wait(5)
        
        self.play(ReplacementTransform(group3b, group4b))

        self.wait(5)

        self.play(Uncreate(group4b))

        self.play(ejemplo2.animate.shift(UP), FadeIn(Tex(r"=")))

        self.wait()

        ejemplo2Def = Tex(r"\textbf{def} nombreFunc($x, y$): \\ \hspace{8em} \textbf{return} $(x^2 + y^2 - 1)^3 - x^2 \cdot y^3$").shift(DOWN)

        self.play(Create(ejemplo2Def))

        self.wait(5)


class temp(Scene):
    def construct(self):
        ejemplo2Def = Tex(r"\textbf{def} nombreFunc($x, y$): \\ \hspace{8em} \textbf{return} $(x^2 + y^2 - 1)^3 - x^2 \cdot y^3$").shift(DOWN)

        self.add(ejemplo2Def)