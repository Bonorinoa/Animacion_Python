from manim import *

class imgTest(Scene):
    def construct(self):

        img = ImageMobject("C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\fastai_logo.png").scale(0.5)
        self.play(Broadcast(img))

        self.clear()
        text3d = Text("Viajar a la 3ra dimension")
        self.play(ShrinkToCenter(Text("Como por ejemplo")))

        self.play(SpiralIn(text3d), run_time=2)
        self.play(Transform(text3d, text3d.set_color(BLUE)))

        self.play(Unwrite(text3d), run_time=3)
