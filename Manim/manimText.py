from manim import *

# All animations must reside within the construct() method of a class derived from Scene. 
# Other code, such as auxiliary or mathematical functions, may reside outside the class.

## Examples with regular text
class textTest(Scene):
    def construct(self):
        text = Text("Hello World", t2c={'[1:-3]': BLUE})
        text2 = Text("What's Popping", t2c={'Pop': RED}).next_to(text, DOWN)
        self.add(text, text2)
        



## Examples with LaTeX
class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r"f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6", font_size=96)
        self.add(tex)
        
class logoTest(Scene):
    def construct(self):
        logo_black = "#343434"
        circle = Circle().shift(2 * DOWN)  # create a circle
        square = Square()
        augusto = MathTex(r"\mathbb{A}", fill_color=logo_black).scale(4)
        gustavo = MathTex(r"\mathbb{G}", fill_color=logo_black).scale(4)
        nombres = Text("Augusto y Gustavo", color = RED)
        text = Text("Python Integral", color="#00FFFF").shift(UP).add_background_rectangle(color=BLUE, opacity=0.4)  # create a square

        self.play(Create(square))  # show the square on screen
        self.add(augusto)
        self.wait(1)
        self.play(ReplacementTransform(augusto, gustavo))
        self.play(square.animate.rotate(PI/6))  # rotate the square
        self.wait(1)
        self.remove(gustavo)
        self.play(
            ReplacementTransform(square, text)
        )  # transform the square into text
        self.play(Create(circle))
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
        self.play(ReplacementTransform(circle, nombres))
        self.wait(2)

