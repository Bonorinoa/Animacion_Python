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