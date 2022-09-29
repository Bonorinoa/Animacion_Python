from manim import *
from manim.opengl import *
import numpy as np

class OpenGLIntro(Scene):
    def construct(self):
        hello_world = Tex("Hello World!").scale(3)
        self.play(Write(hello_world))
        self.play(Rotate(hello_world))
        self.play(
            self.camera.animate.set_euler_angles(
                theta=-10*DEGREES,
                phi=50*DEGREES
            )
        )
        self.wait(5)
        
        self.play(FadeOut(hello_world))
        
        cubo = Cube(fill_color=YELLOW)
        self.play(FadeIn(cubo))
        self.wait(7)
        
        self.play(Uncreate(cubo))  
        
        ax = ThreeDAxes()
        esfera = Surface(
                lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)

        )
        
        self.play(Create(ax), Create(esfera))
        self.play(self.renderer.camera.light_source.animate.move_to(3*IN), run_time=2)
        self.wait(3)

        self.play(
            self.camera.animate.set_euler_angles(
                theta=-50*DEGREES,
                phi=30*DEGREES
            )
        )
        
        surface = OpenGLSurface(
            lambda u, v: (u, v, u*np.sin(v) + v*np.cos(u)),
            u_range=(-3, 3),
            v_range=(-3, 3), color=BLUE
        )
        #surface_mesh = OpenGLSurfaceMesh(surface)
        self.play(Create(surface))
        #self.play(FadeTransform(surface_mesh, surface))
        self.wait()
        light = self.camera.light_source
        self.play(light.animate.shift([0, 0, -20]))
        self.play(light.animate.shift([0, 0, 10]))
        self.play(self.camera.animate.set_euler_angles(theta=60*DEGREES))
        
        self.interactive_embed()

# Pyglet docs: https://pyglet.org/
# Scipy docs: https://scipy.org/
# Source: https://github.com/ManimCommunity/manim/blob/main/example_scenes/opengl.py

class SurfaceExample(Scene):
    
    # agregar funcion que permita avanzar la animacion al cliquear N

    def construct(self):

        torus1 = Torus(major_radius=1, minor_radius=1)
        torus2 = Torus(major_radius=3, minor_radius=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)
        # You can texture a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        day_texture = "C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\1280px-The_earth_at_night"
        night_texture = "C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\1280px-The_earth_at_night.jpg"

        surfaces = [
            OpenGLTexturedSurface(surface, day_texture, night_texture)
            for surface in [sphere, torus1, torus2]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = OpenGLSurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        # Set perspective
        frame = self.renderer.camera
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            Create(surface.mesh, lag_ratio=0.01, run_time=3),
        )
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(Transform(surface, surfaces[1]), run_time=3)

        self.play(
            Transform(surface, surfaces[2]),
            # Move camera frame during the transition
            frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=3,
        )
        # Add ambient rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3 * IN), run_time=5)
        self.play(light.animate.shift(10 * OUT), run_time=5)
        
        self.interactive_embed()

class NewtonIteration(Scene):
    def construct(self):
        ax = Axes()
        #f = lambda x: x**2 + 3*x**3
        curve = ax.plot(lambda x: x**2 + 3*x**3, color=YELLOW)
        cursor_dot = OpenGLDot(color=RED)
        self.add(curve)
        self.play(Create(ax), FadeIn(cursor_dot))
        self.interactive_embed()  # not supported in online environment

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key as pyglet_key
        from scipy.misc import derivative
        if symbol == pyglet_key.P:
            x, y = self.axes.point_to_coords(self.mouse_point.get_center())
            self.play(
                self.cursor_dot.animate.move_to(self.axes.c2p(x, self.f(x)))
            )

        if symbol == pyglet_key.I:
            x, y = self.axes.point_to_coords(self.cursor_dot.get_center())
            # Newton iteration: x_new = x - f(x) / f'(x)
            x_new = x - self.f(x) / derivative(self.f, x, dx=0.01)
            curve_point = self.cursor_dot.get_center()
            axes_point = self.axes.c2p(x_new, 0)
            tangent = Line(
                curve_point + (curve_point - axes_point)*0.25,
                axes_point + (axes_point - curve_point)*0.25,
                color=YELLOW,
                stroke_width=2,
            )
            self.play(Create(tangent))
            self.play(self.cursor_dot.animate.move_to(self.axes.c2p(x_new, 0)))
            self.play(
                self.cursor_dot.animate.move_to(self.axes.c2p(x_new, self.f(x_new))),
                FadeOut(tangent)
            )
        
        super().on_key_press(symbol, modifiers)