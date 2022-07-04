from manim import *

# Todas las animaciones debes estar dentro del metodo construct() de tu clase. 
# Otro codigo, como auxiliar o funciones matematicas, pueden definirse fuera.
class CrearMObjects(Scene):
    def construct(self):
        circulo = Circle()  # instanciar circulo
        circulo.set_fill(color=PINK, opacity=0.5)  # especificar color y transparencia
        
        triangulo = Triangle(color=GREEN)
        polygono = RegularPolygon(n=3, color=RED_A)

        self.add(circulo)  # agregar circulo a la Scene
        self.add(triangulo.shift(RIGHT)) # agregar triangulo a la derecha del centro
        self.play(Create(polygono.next_to(triangulo, DOWN))) # crear polygono abajo de triangulo

        self.wait(2) # esperar 2 segundos antes de cortar video

class ShowScreenResolution(Scene):
    def construct(self):  
        # 1080 es el default
        pixel_alto = config["pixel_height"]
        # 1920 es el default
        pixel_ancho = config["pixel_width"]  
        frame_ancho = config["frame_width"]
        frame_alto = config["frame_height"]
        # punto en origen
        self.add(Dot(), Text(str(ORIGIN)).scale(0.75).shift(UP))
        
        d1 = Line(frame_ancho * LEFT / 2, frame_ancho * RIGHT / 2).to_edge(DOWN)
        self.add(d1)
        self.add(Text(str(pixel_ancho)).next_to(d1, UP))
        d2 = Line(frame_alto * UP / 2, frame_alto * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(Text(str(pixel_alto)).next_to(d2, RIGHT))

class PosTransf(Scene):
    def construct(self):
        circle = Circle().shift(2 * DOWN)  # create a circle
        square = Square()
        text = Text("Ahora soy un texto").shift(UP)
        text.add_background_rectangle(color=BLUE, opacity=0.4)

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, text)
        )  # transform the square into text
        self.play(Create(circle))
        self.play(Transform(text, Text("En una animacion sobre movimiento")))
        
        posiciones = [LEFT*3, UP, DR*2, UR, DL*6, RIGHT*4, DOWN*2]
        for pos in posiciones:
            self.play(circle.animate.move_to(pos))
        
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen