from manim import *

class colorFondo(Scene):
    def construct(self):

        titulo = Title("Fundamentos de Camera")

        self.add(titulo)

        self.wait(3)

        self.camera.background_color = WHITE

        self.wait(3)

        self.play(titulo.animate.set_color(BLACK))

        self.wait(3)

class imgFondo(Scene):
    def construct(self):

        background = ImageMobject('C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\carina-nebula-webb-1.png')

        texto = Title("Una clase en el espacio")

        self.add(background)
        self.bring_to_back(background)

        self.play(Create(texto))

        self.wait(2)

        self.play(Uncreate(texto))

        background2 = ImageMobject('C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\webb.png')
        self.remove(background)

        self.add(background2)
        self.bring_to_back(background2)

        self.wait(2)

        background3 = ImageMobject('C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\galaxias.png')
        self.remove(background2)

        self.add(background3)
        self.bring_to_back(background3)

        self.wait(2)

        background4 = ImageMobject('C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\supernova.png')
        self.remove(background3)

        self.add(background4)
        self.bring_to_back(background4)

        self.wait(4)

class testFondo(Scene):
    def construct(self):

        background = 'C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\carina-nebula-webb-1.png'
      
        self.camera = Camera(background_image=background)
