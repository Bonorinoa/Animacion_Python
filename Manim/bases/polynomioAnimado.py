from manim import *

class MonoToPoly(Scene):
    def construct(self):

        eq1 = MathTex(r"f_1(x) = 3x^4").shift(4*LEFT)
        eq2 = MathTex(r"f_2(x) = -x^7")
        eq3 = MathTex(r"f_3(x) = -10x^2").shift(4*RIGHT)
        eqs = VGroup(eq1, eq2, eq3)

        poly = MathTex(r"h(x) = 3x^4 - x^7 - 10x^2")

        text1 = Text("Monomials").shift(2*UP)
        text2 = Text("Polynomial").shift(2*UP)

        self.add(text1)
        self.add(eqs)
        self.wait(2)
        self.play(ReplacementTransform(text1, text2))
        self.play(ReplacementTransform(eqs, poly))
        self.wait(3)