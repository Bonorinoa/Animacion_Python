from manim import * 
import pandas as pd

# Data en PBI por pais:
# https://databank.worldbank.org/reports.aspx?source=2&series=NY.GDP.MKTP.CD&country=#

# Usar de ejemplo para mostrar thread error al animar
class funcProb(Scene):
   
    def func(self, t):
        return np.array([np.sin(10*t), np.sin(8*t), 0])

    def construct(self):
        func = ParametricFunction(self.func, t_range = np.array([0, 10]),
                 fill_opacity=0).set_color(RED).scale(1.5)
        # cambiar por self.play(Create(func))
        self.add(func)
        self.wait(2)

# Alternativa de lambda para animar funciones 
class funcProb2(Scene):

    def construct(self):

        titulo1 = Title("Funciones Paramétricas")
        self.add(titulo1)

        func = ParametricFunction(
                 lambda t: np.array([np.sin(10*t), np.sin(8*t), 0]),
                 t_range = np.array([0, 10]),
                 fill_opacity=0).set_color(RED).scale(1.5)

        funcText = MathTex(r"x(t) &= sin(10\cdot t) \\ y(t) &= sin(8\cdot t)").next_to(titulo1, DOWN).to_edge(LEFT)

        self.play(Create(func), Write(funcText), run_time=6)
        self.wait(2)

        astroid = ParametricFunction(
                    lambda t: np.array([np.cos(t*5), np.sin(t)**3, 0]),
                    t_range = np.array([0, 7]),
                    fill_opacity=0).set_color(BLUE_B).scale(1.5)

        astroidText = MathTex(r"x(t) &= cos(5\cdot t) \\ y(t) &= sin(t)^3").next_to(titulo1, DOWN).to_edge(LEFT)
        
        self.play(Unwrite(funcText))
        self.wait()
        self.play(Write(astroidText))
        self.play(ReplacementTransform(func, astroid), run_time=6)
        self.wait(2)

        # include one or two implicit functions

        titulo2 = Title("Funciones Implícitas")

        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        ).scale(0.7)

        corazon = ImplicitFunction(
            lambda x,y: (x**2 + y**2 - 1)**3 - x**2 * y**3,
            color=RED
        )

        corText = MathTex(r"f(x,y) = (x^2 + y^2 - 1)^3 - x^2 \cdot y^3").next_to(titulo2, DOWN).to_edge(LEFT)

        numPlane = NumberPlane().scale(0.7)

        corGroup = VGroup(numPlane, corazon, corText)

        self.play(Uncreate(titulo1), Create(titulo2))
        self.play(Unwrite(astroidText), Write(corText))
        self.wait()
        self.play(ReplacementTransform(astroid, corGroup), run_time=5)

        self.wait(2)

        # Sin Cos

        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)

        self.play(Uncreate(corGroup))
        self.play(Create(plot), FadeIn(labels), run_time=5)

        self.wait(2)

        self.clear()

        # Probability examples

        titulo3 = Title("Probabilidad y Gráficos estadísticos")
        self.add(titulo3)

        values = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

        chart = BarChart(
            values,
            y_range=[-10, 10, 2],
            y_axis_config={"font_size": 24},
        )

        chart.change_bar_values(list(reversed(values)))
        self.play(Create(chart))

        barLabels = chart.get_bar_labels(font_size=24)

        self.play(FadeIn(barLabels))
        self.wait(5)
        self.play(FadeOut(barLabels))

        # BarChart con data real

        data = pd.read_csv("gdp_per_country.csv")

        paises = ["Argentina", "Chile", "Uruguay", "Brazil", "Finland", "France", "Germany", "Spain"]

        cleanedData = data.query("`Country Name` in @paises")

        cambioGDP = round((cleanedData["2021"].astype(float) - cleanedData["2020"].astype(float)) / 1000000, 2)

        chart2 = BarChart(
            cambioGDP,
            x_axis_config={"font_size": 20},
        )

        y_label = chart2.get_y_axis_label(Text("GDP (Millones u$d)").scale(0.7).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,)

        self.play(ReplacementTransform(chart, chart2))

        self.play(FadeIn(chart2.get_bar_labels(font_size=24)), FadeIn(y_label))

        self.wait(5)

        self.play(FadeOut(chart2.get_bar_labels(font_size=24)))

        self.wait(5)