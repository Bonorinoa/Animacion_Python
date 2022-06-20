from manim import *

# All animations must reside within the construct() method of a class derived from Scene. 
# Other code, such as auxiliary or mathematical functions, may reside outside the class.
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen