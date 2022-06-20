from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle().shift(2 * DOWN)  # create a circle
        square = Square()
        text = Text("I am now a text").shift(UP).add_background_rectangle(color=BLUE, opacity=0.4)  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, text)
        )  # transform the square into text
        self.play(Create(circle))
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen