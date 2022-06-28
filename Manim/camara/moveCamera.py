from manim import *

class cameraTest(ThreeDScene):
    def construct(self):

        text3d = Text("Bienvenidos a la 3ra dimension", color=ORANGE)
        self.play(Write(text3d), run_time=2)
        
        ## MObjects in 3D
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        
        self.wait(2)

        self.move_camera(phi=360 * DEGREES, theta=270 * DEGREES)
        self.play(Unwrite(text3d), run_time=2)
        self.wait(1)