from manim import *


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