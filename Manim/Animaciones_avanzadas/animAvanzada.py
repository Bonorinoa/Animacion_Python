from manim import *

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.add(Title("Un ejemplo de animacion mecanica"))
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()
        

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.45

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(5)

        dot.remove_updater(go_around_circle)

# segundo ejemplo
class CalculusSlopes(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-3, 3], y_range=[-4, 14], y_length=7, x_length=6
        ).add_coordinates()

        graph1 = plane.plot(lambda x: x ** 2, x_range=[-3, 3], color=RED)
        graph1_lab = (
            MathTex("f(x)={x}^{2}")
            .next_to(graph1, UR, buff=0.2)
            .set_color(RED)
            .scale(0.8)
        )

        c = ValueTracker(-4)

        graph2 = always_redraw(
            lambda: plane.plot(
                lambda x: x ** 2 + c.get_value(), x_range=[-3, 3], color=YELLOW
            )
        )

        graph2_lab = always_redraw(
            lambda: MathTex("f(x)={x}^{2}")
            .next_to(graph2, UR, buff=0.2)
            .set_color(YELLOW)
            .scale(0.8)
        )

        c_label = DecimalNumber(include_sign=True).set_color(YELLOW).scale(0.8)
        c_label.add_updater(lambda y: y.set_value(c.get_value()).next_to(graph2_lab, RIGHT))


        k = ValueTracker(-3)
        dot1 = always_redraw(
            lambda: Dot().move_to(
                plane.coords_to_point(
                    k.get_value(), graph1.underlying_function(k.get_value())
                )
            )
        )
        slope1 = always_redraw(
            lambda: plane.get_secant_slope_group(
                x=k.get_value(), graph=graph1, dx=0.01, secant_line_length=5
            )
        )

        slope2 = always_redraw(
            lambda: plane.get_secant_slope_group(
                x=k.get_value(), graph=graph2, dx=0.01, secant_line_length=5
            )
        )
        dot2 = always_redraw(
            lambda: Dot().move_to(
                plane.coords_to_point(
                    k.get_value(), graph2.underlying_function(k.get_value())
                )
            )
        )

        self.add(plane)

        self.play(Create(VGroup(graph1, graph2)))
        self.add(slope1, slope2, dot1, dot2, graph1_lab, graph2_lab, c_label)
        self.play(
            k.animate.set_value(0), c.animate.set_value(2), run_time=5, rate_func=linear
        )
        self.play(
            k.animate.set_value(3),
            c.animate.set_value(-2),
            run_time=5,
            rate_func=linear,
        )
        self.wait()


class CalculusArea(Scene):
    
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[0]),
            (top_right[0], bottom_left[0]),
        ]

    def construct(self):

        axes = Axes(
            x_range=[-5, 5], x_length=8, y_range=[-7, 7], y_length=7
        ).add_coordinates()

        graph = axes.plot(
            lambda x: 2*x**3, x_range=[-5, 5], color=YELLOW
        )
        self.add(axes, graph)

        dx_list = [1, 0.5, 0.3, 0.1, 0.05, 0.025, 0.01]
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=graph,
                    x_range=[-5, 5],
                    stroke_width=0.1,
                    stroke_color=WHITE,
                    dx=dx, fill_opacity=0.7
                )
                for dx in dx_list
            ]
        )
        first_area = rectangles[0]
        for k in range(1, len(dx_list)):
            new_area = rectangles[k]
            self.play(Transform(first_area, new_area), run_time=3)
            self.wait(0.5)

        self.wait(3)

        self.clear()

        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )

        t = ValueTracker(5)
        k = 25

        graph = ax.plot(
            lambda x: k / x,
            color=YELLOW_D,
            x_range=[k / 10, 10.0, 0.01],
            use_smoothing=False,
        )

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (t.get_value(), k / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon

        polygon = always_redraw(get_rectangle)

        dot = Dot()
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k / t.get_value())))
        dot.set_z_index(10)

        group = VGroup(ax, graph, dot, polygon)

        self.play(Create(group))
        self.play(t.animate.set_value(10))
        self.play(t.animate.set_value(k / 10))
        self.play(t.animate.set_value(5))
