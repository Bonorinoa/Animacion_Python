from manim import *

class CodeFromString(Scene):
    def construct(self):
        code = '''from manim import *

class PosTransf(Scene):
    def construct(self):
        circle = Circle().shift(2 * DOWN)
        square = Square()
        texto1 = Text("Ahora soy un texto").shift(UP)
        texto1.add_background_rectangle(color=BLUE, opacity=0.4)

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4)) # rotar cuadrado
        # transformar cuadrado en texto1
        self.play( ReplacementTransform(square, texto1) ) 
        self.play(Create(circle))
        # transformar texto1 en nuevo texto
        self.play(Transform(texto1,
            Text("En una animacion sobre movimiento")))
        # Animacion de varias ubicaciones constantes en Scene
        posiciones = [LEFT*3, UP, DR*2, UR, DL*6, RIGHT*4, DOWN*2]
        for pos in posiciones:
            self.play(circle.animate.move_to(pos))
        
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        ) # coloreado animado del circulo
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", line_spacing=0.5, style="dracula", font="Monospace")
        self.add(rendered_code.scale(0.78))
