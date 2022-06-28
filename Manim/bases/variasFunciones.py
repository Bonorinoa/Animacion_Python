from manim import *

class DifferentFunctions(Scene):
    def construct(self):

        rat = MathTex(r"y_1 = \frac{x^2 + 1}{x - 1}").shift(2*LEFT)
        rat2 = MathTex(r"y_2 = \frac{x^5 + 7x}{5}").shift(2*RIGHT)

        expn = MathTex(r"y_1 = 10^x").shift(LEFT*2)
        expn2 = MathTex(r"y_2 = \frac{3x}{2} + e^x").shift(2*RIGHT)

        trig = MathTex(r"y_1 = sin(x)").shift(LEFT*2)
        trig2 = MathTex(r"y_2 = cos(x) - sin(2x)").shift(2*RIGHT)
        
        rats = VGroup(rat, rat2)
        expns = VGroup(expn, expn2)
        trigs = VGroup(trig, trig2)

        text1 = Text("Rational functions").shift(2*UP)
        text2 = Text("Exponential functions").shift(2*UP)
        text3 = Text("Trigonometric functions").shift(2*UP)

        self.add(text1)
        self.add(rats)
        self.wait(2)
        self.play(ReplacementTransform(text1, text2))
        self.play(ReplacementTransform(rats, expns))
        self.wait(2)
        self.play(ReplacementTransform(text2, text3))
        self.play(ReplacementTransform(expns, trigs))
        self.wait(3)