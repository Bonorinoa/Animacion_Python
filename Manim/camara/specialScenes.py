from manim import *

class surfearCurva(MovingCameraScene):
    def construct(self):

        titulo = Title("Moving Camera Scene")

        # Guardar estado original de la lente
        self.camera.frame.save_state()

        # create the axes and the curve
        ejes = Axes()

        """ astroid = ParametricFunction(
            lambda t: np.array([np.cos(t*5), np.sin(t)**3, 0]),
            t_range = np.array([0, 7]),
            fill_opacity=0).set_color(BLUE_B).scale(1.5)
 """
        curva = ejes.plot_parametric_curve(lambda t: np.array([np.cos(t*5), np.sin(t)**3, 0]),
            t_range = np.array([0, 7]),
            fill_opacity=0).set_color(BLUE_B).scale(2)

        # create dots based on the graph
        puntoAmover = Dot(ejes.i2gp(curva.t_min, curva), color=YELLOW)
        punto_1 = Dot(ejes.i2gp(curva.t_min, curva)).set_color(GREEN)
        

        self.add(ejes, curva, punto_1, puntoAmover, titulo)
        self.play(self.camera.frame.animate.scale(0.5).move_to(puntoAmover))

        def update_curva(mob):
            mob.move_to(puntoAmover.get_center())

        self.camera.frame.add_updater(update_curva)
        self.play(MoveAlongPath(puntoAmover, curva, rate_func=rate_functions.double_smooth), run_time=6)
        self.play(puntoAmover.animate.set_color(RED))
        self.camera.frame.remove_updater(update_curva)

        # Restaurar a estado original
        # al final de la animacion
        self.play(Restore(self.camera.frame))

# ZoomedCamera

class zoomEcuacion(ZoomedScene):

    def construct(self):

        titulo = Title("Zoomed Scene")

        eq = MathTex("y ", " = ", " m ", " x ", " + ", " b ").to_corner(UL).shift(DOWN)

        frame_text = Text("Frame", color=BLUE, font_size=30)
        zoomed_camera_text = Text("Zoomed frame", color=GREEN, font_size=30)

        self.add(eq, titulo)

        camara_zoom = self.zoomed_camera
        display_zoom = self.zoomed_display

        frame = camara_zoom.frame
        frame_zoom = display_zoom.display_frame

        frame.move_to(eq[0])
        frame.set_color(BLUE)

        frame_zoom.set_color(GREEN)
        display_zoom.move_to(ORIGIN)

        zd_rect = BackgroundRectangle(display_zoom, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(display_zoom))

        frame_text.next_to(frame, DR)

        self.play(Create(frame), FadeIn(frame_text, shift=UP))
        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)

        zoomed_camera_text.next_to(frame_zoom, DOWN)
        self.play(FadeIn(zoomed_camera_text, shift=UP))     


        # Scale in        x   y  z
        scale_factor = [1, 1, 0]
        self.play(
            frame.animate.scale(scale_factor),
            display_zoom.animate.scale(scale_factor),
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )

        self.wait()

        texto = Text("Variable \n Dependiente", color=GREEN).next_to(frame_zoom, DOWN)
        self.play(ScaleInPlace(display_zoom, 1.1))
        self.play(ReplacementTransform(zoomed_camera_text, texto))
        self.wait()

        texto2 = Text("Variable \n Independiente", color=GREEN).next_to(frame_zoom, DOWN)
        self.play(frame.animate.move_to(eq[3]))
        self.play(ReplacementTransform(texto, texto2))
        self.wait()

        texto3 = Text("Pendiente", color=GREEN).next_to(frame_zoom, DOWN)
        self.play(frame.animate.move_to(eq[2]))
        self.play(ReplacementTransform(texto2, texto3))
        self.wait()

        texto4 = Text("Intercepcion en Y", color=GREEN).next_to(frame_zoom, DOWN)
        self.play(frame.animate.move_to(eq[5]))
        self.play(ReplacementTransform(texto3, texto4))
        self.wait()

        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(frame_zoom), FadeOut(frame))
        self.wait()

        texto5 = Text("Una ecuación lineal")

        self.play(ReplacementTransform(texto4, texto5))

        self.wait(3)

# ThreeDScene

class ejemplos3D(ThreeDScene):
    def construct(self):

        titulo = Title("Escenas en 3D")

        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)

        ejes3D = ThreeDAxes()
        self.add(ejes3D,gauss_plane)

        self.begin_3dillusion_camera_rotation(rate=1)
        self.wait(PI/2)
        self.stop_3dillusion_camera_rotation()
        self.wait(2)

        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait(2)

        esfera = Surface(
                lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)

        )
        self.play(Create(ThreeDAxes()), ReplacementTransform(gauss_plane, esfera), run_time=3)

        self.play(self.renderer.camera.light_source.animate.move_to(3*IN), run_time=2)
        self.wait(3)
        self.play(self.renderer.camera.light_source.animate.move_to(2*OUT), run_time=2)
        self.wait(2)

        param = ParametricFunction(
            lambda t: np.array([np.sin(7*t), -np.cos(t**2), np.cos(t)]),
            t_range = np.array([0, 4]),
            fill_opacity=0).set_color(PURPLE).scale(1.5)
        
        self.play(ReplacementTransform(esfera, param), run_time=2)
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(2)
        
        
