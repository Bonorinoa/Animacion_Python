from manim import *
        
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