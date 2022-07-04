from manim import *

class BasesEjes(Scene):
    def construct(self):
        ejes = Axes().scale(0.75).shift(DOWN)
        titulo = Title("Fundamentos de Ejes de Coordenadas")

        intro = Text("Instanciar Axes() con argumentos predeterminados resulta en lo siguiente: ", font_size=20).next_to(titulo, DOWN).to_edge(LEFT)

        grupo0 = VGroup(intro, ejes)

        self.play(Create(titulo), Create(grupo0))

        self.wait(5)

        texto0 = Text("Sin embargo puede usarse para crear gráficos más complejos. Por ejemplo,", font_size=20).next_to(titulo, DOWN)

        ax = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 10, 1],
            tips = False,
            axis_config={"include_numbers": False},
        )

        # Labels for the x-axis and y-axis.
        y_label = ax.get_y_axis_label("x_2", buff=0.4)
        x_label = ax.get_x_axis_label("x_1")
        grid_labels = VGroup(x_label, y_label)
        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Canasta de bienes para analisis economico",
            include_underline=False,
            font_size=40,
        )

        dot1 = Dot(ax.coords_to_point(2, 6), color=WHITE)
        dot2 = Dot(ax.coords_to_point(5, 3), color=WHITE)

        lines1 = ax.get_lines_to_point(ax.c2p(2, 6))
        lines2 = ax.get_lines_to_point(ax.c2p(5, 3))

        coords1 = np.around(ax.point_to_coords(dot1.get_right()))
        coords2 = np.around(ax.point_to_coords(dot2.get_right()))

        label1 = (
            Matrix([[coords1[0]], [coords1[1]]]).scale(0.55).next_to(dot1, RIGHT)
        )

        label2 = (
            Matrix([[coords2[0]], [coords2[1]]]).scale(0.55).next_to(dot2, RIGHT)
        )

        grupo1 = VGroup(ax, title, grid_labels, dot1, lines1, dot2, lines2, label1, label2).scale(0.7).shift(DOWN)

        self.play(Write(texto0), ReplacementTransform(grupo0, grupo1))

        self.wait(5)

        ax1 = Axes(y_range=[0, 8], x_range=[2, 5, 0.5] , tips=False, 
             axis_config={"include_numbers": False}).add_coordinates()
        title1 = Title(r"Curvas de Indiferencia", include_underline=False, font_size=40)

        curves = VGroup()
        curves += ax1.plot(lambda x: 15 / x, color=WHITE)
        curves += ax1.plot(lambda x: 10 / x, color=WHITE)
        curves += ax1.plot(lambda x: 5 / x, color=WHITE)

        label_1 = ax1.get_graph_label(curves[0], MathTex(r"\frac{15}{x}", font_size=25), x_val=4, direction=UP)
        label_2 = ax1.get_graph_label(curves[1], MathTex(r"\frac{10}{x}", font_size=25), x_val=3, direction=DOWN)
        label_3 = ax1.get_graph_label(curves[2], MathTex(r"\frac{5}{x}", font_size=25), x_val=2.5, direction=DOWN)
        labels = VGroup(label_1, label_2, label_3)

        grupo2 = VGroup(ax1, title1, curves, labels).scale(0.7).shift(DOWN)

        self.play(ReplacementTransform(grupo1, grupo2))

        self.wait(5)

        texto1 = Text("Incluso animar el comportamiento de un algoritmo que busque el mínimo local", font_size=20).next_to(titulo, DOWN)

        ax2 = Axes(
            x_range=[2, 8], y_range=[0, 100, 10], axis_config={"include_tip": True}
        ).add_coordinates()

        ylabel = ax2.get_y_axis_label(Tex("Loss").scale(0.8).rotate(90 * DEGREES), edge=LEFT, direction=LEFT*2, buff=0.5)
        xlabel = ax2.get_x_axis_label( Tex("Weight").scale(0.8), edge=DOWN, direction=DOWN*2, buff=0.5)

        labels2 = VGroup(ylabel, xlabel)

        title2 = Title(
            r"Animación de Gradient Descent $y=8 \cdot ( x - 5)^{ 2 } + 10$",
            include_underline=True,
            font_size=45
        )

        backgroundRectangle = BackgroundRectangle(title2, color=YELLOW, fill_opacity=0.25)

        t = ValueTracker(2.5)
        t_2 = ValueTracker(7.5)

        def func(x):
            return 8 * (x - 5)**2 + 10

        graph = ax2.plot(func, color=WHITE)

        line_1 = ax2.get_vertical_line(ax2.input_to_graph_point(6, graph), color=YELLOW)
        line_2 = ax2.get_vertical_line(ax2.input_to_graph_point(4, graph), color=YELLOW)

        def linear(x):
            return 16*x - 78

    
        def linear2(x):
            return -16*x + 82
    
        linear_graph = ax2.plot(linear, color=BLUE)
        linear_graph2 = ax2.plot(linear2, color=BLUE)


        initial_point = [ax2.coords_to_point(t.get_value(), func(t.get_value()))]
        #point_2 = [ax2.coords_to_point(t_2.get_value(), func(t_2.get_value()))]
        dot = Dot(radius=.15, point=initial_point, color=RED)
        #dot2 = Dot(point=point_2)

        def dot_position(mobject):
            mobject.set_value(dot.get_coord(dim=2))
            mobject.next_to(dot, UP)


        dot.add_updater(lambda x: x.move_to(ax2.c2p(t.get_value(), func(t.get_value()))))
        dotLabel = DecimalNumber(font_size=24)
        dotLabel.add_updater(lambda l: l.set_value(t.get_value()+0.02).next_to(dot, UP))
        #lambda l: l.set_value(dot.get_x)

        x_space = np.linspace(*ax2.x_range[:2], 200)
        minimum_index = func(x_space).argmin()

        grupo3 = VGroup(ax2, labels2, graph, title2, backgroundRectangle, dot,
                        linear_graph, linear_graph2, line_1, line_2).scale(0.6)

        self.play(ReplacementTransform(texto0, texto1), ReplacementTransform(grupo2, grupo3))
        self.add(dotLabel)

        self.play(t.animate.set_value(x_space[minimum_index] + 3))
        self.play(t.animate.set_value(x_space[minimum_index] - 3))
        self.play(t.animate.set_value(x_space[minimum_index] + 2.2))
        self.play(t.animate.set_value(x_space[minimum_index] - 2.2))
        self.play(t.animate.set_value(x_space[minimum_index] + 1))


        self.play(Create(line_1, run_time=1))
        self.play(Create(linear_graph, run_time=1))
        self.play(t.animate.set_value(x_space[minimum_index]), run_time=1)


        self.play(t.animate.set_value(x_space[minimum_index] - 1))
        self.play(Create(line_2))
        self.play(Create(linear_graph2))
        self.play(t.animate.set_value(x_space[minimum_index]))


        self.wait(5)