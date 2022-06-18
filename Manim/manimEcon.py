from manim import *

class commodityBundle(Scene):
    def construct(self):
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
            r"Two commodity bundles in commodity space",
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

        self.add(ax, title, grid_labels, dot1, lines1, dot2, lines2, label1, label2)

class indifferenceCurve(Scene):
    def construct(self):

        ax = Axes(y_range=[0, 8], x_range=[2, 5, 0.5] , tips=False, 
             axis_config={"include_numbers": False}).add_coordinates()
        title = Title(r"Indifference Curves", include_underline=False, font_size=35)

        curves = VGroup()
        curves += ax.plot(lambda x: 15 / x, color=WHITE)
        curves += ax.plot(lambda x: 10 / x, color=WHITE)
        curves += ax.plot(lambda x: 5 / x, color=WHITE)

        label_1 = ax.get_graph_label(curves[0], MathTex(r"\frac{15}{x}", font_size=25), x_val=4, direction=UP)
        label_2 = ax.get_graph_label(curves[1], MathTex(r"\frac{10}{x}", font_size=25), x_val=3, direction=DOWN)
        label_3 = ax.get_graph_label(curves[2], MathTex(r"\frac{5}{x}", font_size=25), x_val=2.5, direction=DOWN)
        labels = VGroup(label_1, label_2, label_3)



        self.add(ax, title, curves, labels)

class MonoToPoly(Scene):
    def construct(self):

        eq1 = MathTex(r"f_1(x) = 3x^4").shift(4*LEFT)
        eq2 = MathTex(r"f_2(x) = -x^7")
        eq3 = MathTex(r"f_3(x) = -10x^2").shift(4*RIGHT)
        eqs = VGroup(eq1, eq2, eq3)

        poly = MathTex(r"h(x) = 3x^4 - x^7 - 10x^2")

        text1 = Text("Monomials").shift(2*UP)
        text2 = Text("Polynomial").shift(2*UP)

        self.add(text1)
        self.add(eqs)
        self.wait(2)
        self.play(ReplacementTransform(text1, text2))
        self.play(ReplacementTransform(eqs, poly))
        self.wait(3)

class DifferentFunctions(Scene):
    def construct(self):

        rat = MathTex(r"y_1 = \frac{x^2 + 1}{x - 1}").shift(2*LEFT)
        rat2 = MathTex(r"y_2 = \frac{x^5 + 7x}{5}").shift(2*RIGHT)

        expn = MathTex(r"y_1 = 10^x").shift(LEFT*2)
        expn2 = MathTex(r"y_2 = \frac{3x}{2} + e^x").shift(2*RIGHT)

        trig = MathTex(r"y_1 = sin(x)").shift(LEFT*2)
        trig2 = MathTex(r"y_2 = cos(x) - sin(2x)").shift(2*RIGHT)
        
        rats = VGroup(rat, rat2)
        expns = VGroup(expn, expn2)
        trigs = VGroup(trig, trig2)

        text1 = Text("Rational functions").shift(2*UP)
        text2 = Text("Exponential functions").shift(2*UP)
        text3 = Text("Trigonometric functions").shift(2*UP)

        self.add(text1)
        self.add(rats)
        self.wait(2)
        self.play(ReplacementTransform(text1, text2))
        self.play(ReplacementTransform(rats, expns))
        self.wait(2)
        self.play(ReplacementTransform(text2, text3))
        self.play(ReplacementTransform(expns, trigs))
        self.wait(3)
        
class LocalMinMax(Scene):
    def construct(self):

        ax = Axes().add_coordinates()

        func = ax.plot(lambda x: (x-2)**2 + 1, color=WHITE)
        dot = Dot(ax.coords_to_point(2, 1), color=RED)
        lines = ax.get_lines_to_point(ax.c2p(2,1))

        coords = np.around(ax.point_to_coords(dot.get_right()))
        label = (
            Matrix([[coords[0]], [coords[1]]]).scale(0.35).next_to(dot, UP)
        )

        parab = VGroup(ax, func, dot, lines, label)

        self.add(parab)
        self.wait(1)
        #self.play(VGroup(label).animate(run_time=2))

        ## transform to downward sloping parabola + local max

        ax2 = Axes().add_coordinates()

        func2 = ax2.plot(lambda x: -( (x-2)**2 ) + 1, color=WHITE)
        dot2 = Dot(ax2.coords_to_point(2, 1), color=RED)
        lines2 = ax2.get_lines_to_point(ax2.c2p(2,1))

        coords2 = np.around(ax2.point_to_coords(dot2.get_right()))
        label2 = (
            Matrix([[coords2[0]], [coords2[1]]]).scale(0.35).next_to(dot2, UP)
        )

        parab2 = VGroup(ax2, func2, dot2, lines2, label2)

        self.play(ReplacementTransform(parab, parab2))
        self.wait(2)