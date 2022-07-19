from manim import *

class baseScene(Scene):
    def construct(self):

        self.background_color = BLUE_C

        square = Square()

        self.add(square)
        self.add_subcaption("Soy un cuadrado", duration=1)

        self.wait(3)

        circle = Circle(color=RED_B)

        self.play(Create(circle), subcaption="Yo soy un circulo rojo")

        self.wait(2)

        self.remove(square)

        self.wait(2)

        self.clear()

        self.next_section("Nombre opcional para la seccion")

        self.background_color = WHITE

        titulo2 = Title("Segunda sección")

        triangle = Triangle()
        circle = Circle()

        self.play(SpinInFromNothing(triangle))
        self.wait()

        self.play(ReplacementTransform(triangle, circle))
        self.wait()

        self.play(circle.animate.set_color(BLUE))
        self.wait()

        # seccion vacia, se elimina automaticamente
        self.next_section()

# Ejemplo audio mas animacion personalizada

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

class rocketCountdown(Scene):
    def construct(self):

        titulo = Title("Viaje a Marte")

        audio = "C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Soundtracks\\Rocket_Countdown.mp3"

        numero = DecimalNumber().set_color(ORANGE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        numero.add_updater(lambda number: numero.move_to(ORIGIN))

        self.add(titulo, numero)

        self.wait()

        # Play the Count Animation to count from 10 to 0 in 10 seconds
        self.add_sound(audio)
        self.play(Count(numero, 10, 0), run_time=10, rate_func=linear)


        # cambiar triangle por imagen de cohete
        cohete1 = Triangle(color=BLUE).to_corner(DR)
        cohete2 = Triangle(color=BLUE).to_corner(DL)
        
        cohetes = VGroup(cohete1, cohete2)
        self.play(cohetes.animate.shift(UP*8),
                    Flash(numero, line_length=1,
                    num_lines=30, color=ORANGE, run_time=5,
                    flash_radius=1.5 + SMALL_BUFF, rate_func = rush_from),
                    Uncreate(titulo),
                    run_time=6)

        background = ImageMobject('C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\martehd.png')

        self.clear()

        self.add(background)
        self.bring_to_back(background)

        self.wait(4)

