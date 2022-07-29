from manim import *

class PrimerScript(Scene):
    def construct(self):
        
        cuadrado = Square()
        circuloAzul = Circle(color=BLUE).shift(LEFT*2)
        
        self.add(cuadrado)
        self.play(Create(circuloAzul))
        
        self.wait()
        
        self.play(circuloAzul.animate.set_color(GREEN), Rotate(cuadrado))
        
        self.play(FadeOut(circuloAzul))
        
        self.play(ReplacementTransform(cuadrado, Triangle()))
        
        self.wait(2)