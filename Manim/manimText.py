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
        
