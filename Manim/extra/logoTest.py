from manim import *

class ManimCELogo(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()

        atom = Sphere(radius=2.3, u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU], resolution=(15, 32), fill_opacity=10)

        
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=65 * DEGREES, theta=20 * DEGREES)

        torus1 = Torus(minor_radius=0.08).shift(OUT*0.5)
        torus2 = Torus(minor_radius=0.08).shift(IN*0.5)

        dot_1 = Dot3D(point=ax.coords_to_point(4.3, 0, 0), radius=0.1, color=YELLOW)
        dot_2 = Dot3D(point=ax.coords_to_point(4.3, 0, 1.2), radius=0.1, color=YELLOW)
                

        group = VGroup(ax, torus1.set_color(RED), torus2.set_color(BLUE), atom.set_color(GREEN), dot_1, dot_2)
 
        self.add(group)
        self.play(MoveAlongPath(dot_1, torus2), run_time=2, rate_func=linear)

