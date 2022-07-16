from manim import *
from manim_fonts import *

## Split into various scenes for rapid testing and compiling
## Merge clips with editor once finished

penguin = ImageMobject("C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\penguin.png").shift(DOWN*3.5 + LEFT*4.5).scale(0.7)
penguin2 = ImageMobject("C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\Assets\\Images\\penguin2.png").shift(DOWN*3 + LEFT*5.2).scale(0.7)


class StarWars(ThreeDScene):
    def construct(self):
        self.move_camera(phi=55 * DEGREES)
        with RegisterFont("Montserrat") as fonts:
            text = Text("                   EPISODIO I"
                        "\n\n\nEn una galaxia muy, muy lejana... "
                        "\nYace un joven jedi deseando dominar Python"
                        "\nBuscando inspirar a otros a programar"
                        "\nY a inscribirse en este curso.",
                        
                        font=fonts[0], color=YELLOW, line_spacing=1.5, weight=BOLD).scale(0.85)
        
            self.play(FadeIn(text))
            self.wait(1)
            self.play(text.animate.shift(14*UP), run_time=9)

        self.play(GrowFromPoint(penguin, [-4, -2, 0]))
        saludo = Text("Hola! Soy Dr. Gus").next_to(penguin, UP).scale(0.5)
        self.play(Write(saludo))
        self.play(ApplyWave(penguin), Circumscribe(saludo, time_width=3), run_time=2)
        self.wait(1)

        self.clear()
      
        self.move_camera(phi=55 * DEGREES)  
        texto1 = Text("Permitanme demostrarles algunas de las \nmaravillosas cosas que podemos crear", font_size=30)
        texto2 = Text("Ups, mejor ajustemos la camara", font_size=30).shift(DOWN*2.5)

        self.add(penguin2, texto1)
        self.wait(2)
        self.play(FadeIn(texto2))

        self.move_camera(phi=0 * DEGREES)

        self.wait(2)

        self.play(FadeOut(texto2))

        texto3 = Text("Mejor? Bien, manos a la obra...", font_size=36).shift(DOWN*2)

        self.play(Write(texto3), run_time=2)
        self.play(Uncreate(texto1))
        self.wait(1)

        # Objetos 2D
        texto4 = Text("Ademas de texto, podemos manipular figuras geometricas!", font_size=26)
        
        self.play(FadeTransform(texto3, texto4))

        self.wait(1)

class mobjects2D(ThreeDScene):
    def construct(self):
        some2DMobjects = Group(Circle(), Triangle(), Square(),
                     Star(), Star().round_corners(radius=0.5),
                     RegularPolygon(n=10, color=RED)).scale(0.75)
        
        positions2D = [UL*2, UR*2, DL*2, DR*2, UP*2, DOWN*2]

        group2D = VGroup()
        for pos, mobject in zip(positions2D, some2DMobjects):
            group2D += mobject.shift(pos*1.5)

        self.play(GrowFromCenter(group2D))

        texto5 = Text("Las podemos hacer bailar")

        self.play(GrowFromCenter(texto5))
        self.play(ApplyWave(some2DMobjects), run_time=2)

        texto6 = Text("Las podemos hacer rotar")

        self.play(ReplacementTransform(texto5, texto6))
        self.play(Rotate(some2DMobjects, PI*4), run_time=2)

        self.wait(1)

        self.play(Uncreate(texto6))

        texto7 = Text("Y mucho mas!")

        self.play(Indicate(texto7))
        self.play(FadeOut(some2DMobjects))
        self.play(Unwrite(texto7))

class mobjects3D(ThreeDScene):
    def construct(self):
        # Objetos 3D

        some3DMobjects = Group(Dodecahedron(), Icosahedron().set_color("#4c7fff"),
                          Cube().set_color(YELLOW_A), Sphere().set_color(RED), Cone().set_color(ORANGE),
                          Prism()).scale(0.75)

        positions3D = [LEFT*2, RIGHT*2, DL*2, DR*2, UP, DOWN]

        group3D = VGroup()
        for pos, mobject in zip(positions3D, some3DMobjects):
            group3D += mobject.shift(pos*1.5)

        self.play(FadeIn(group3D))

        self.wait(1)

        self.play(ApplyWave(some3DMobjects), run_time=2)

        ## MObjects in 3D
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(ThreeDAxes())

        self.play(Rotate(some3DMobjects, -PI*4), run_time=2)

        self.wait(2)

class linearAlgebra(Scene):
    def construct(self):

        # Linear Algebra

        texto10 = Text("Creemos un plano numerico").to_corner(UL).scale(0.5)
        texto11 = Text("Con algunos vectores").to_corner(UL).scale(0.5)
        texto12 = Text("Y una simple suma vectorial").to_corner(UL).scale(0.5)
        
        plane = NumberPlane()

        vec_1 = Vector([1, 2])
        vec_2 = Vector([-3, -2], color=YELLOW)
        vec_3 = Arrow(start=[-3, -2, 0], end=[1,2,0], color=RED)
        label_1 = vec_1.coordinate_label()
        label_2 = vec_2.coordinate_label(color=YELLOW)
        #label_3 = vec_3.coordinate_label(color=RED)

        self.play(Create(texto10), Create(plane))
        self.play(ReplacementTransform(texto10, texto11), Create(vec_1), FadeIn(label_1))
        self.play(Create(vec_2), FadeIn(label_2))

        v1 = Tex(r"\[a = \begin{bmatrix} 1 \\ 2 \end{bmatrix}\]")
        v2 = Tex(r" \[+\begin{bmatrix} -3 \\ -2 \end{bmatrix}\]").next_to(v1, RIGHT)
        res = Tex(r" \[= \begin{bmatrix} -2 \\ 0 \end{bmatrix}\]", color=RED).next_to(v2, RIGHT)

        self.play(ReplacementTransform(texto11, texto12), Create(VGroup(v1, v2, res).to_corner(UL*2).scale(0.65)))
        self.play(Create(vec_3))

        self.wait(1)

        transform1 = Tex("Seguido de una transformacion lineal")
        transform2 = Matrix([[1, 1], [0, 0.66]], left_bracket="(", right_bracket=")").next_to(transform1, RIGHT)
        self.play(ReplacementTransform(VGroup(v1, v2, res, texto12, label_1, label_2), VGroup(transform1, transform2).to_corner(UL*2).scale(0.65)))

        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, VGroup(vec_1, vec_2, vec_3)), ApplyMatrix(matrix, plane))
        self.wait(1)

        # Vector Field
        texto14 = Text("Ahora un campo vectorial", weight=BOLD).to_corner(UL).scale(0.5)

        self.remove(plane)
        self.play(ReplacementTransform(VGroup(vec_1, vec_2, vec_3, transform1, transform2), texto14), Create(Axes()))

        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()

        texto15 = Text("Cuyo flow puede ser facilmente ilustrado", weight=BOLD).to_corner(UL).scale(0.5)
        self.play(ReplacementTransform(texto14, texto15))

        stream_lines = StreamLines(
            func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
        )
 
        spawning_area = Rectangle(width=6, height=4)
        flowing_area = Rectangle(width=8, height=6)
           
        labels = [Tex("Area de desove"), Tex("Area de flow").shift(DOWN * 2.5)]
        for lbl in labels:
            lbl.add_background_rectangle(opacity=0.6, buff=0.05)

        self.play(FadeOut(ArrowVectorField(func)))
        self.play(Create(VGroup(stream_lines, spawning_area, flowing_area, *labels)))
        self.wait(3)

class GradientDescent(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="Weight", y_label="Loss")
        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Gradient Descent animation for $y=8 \cdot ( x - 5)^{ 2 }$",
            include_underline=False,
            font_size=35
        )
        backgroundRectangle1 = BackgroundRectangle(title, color=YELLOW, fill_opacity=0.25)

        t = ValueTracker(1.5)
        t_2 = ValueTracker(8.5)

        def func(x):
            return 8 * (x - 5)**2 + 10

        graph = ax.plot(func, color=WHITE)

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(6.5, graph), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.input_to_graph_point(3.5, graph), color=YELLOW)

        def linear(x):
            return 25*x - 135

    
        def linear2(x):
            return -25*x + 115
    
        linear_graph = ax.plot(linear, color=BLUE)
        linear_graph2 = ax.plot(linear2, color=BLUE)


        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        point_2 = [ax.coords_to_point(t_2.get_value(), func(t_2.get_value()))]
        dot = Dot(radius=.15, point=initial_point, color=RED)
        dot2 = Dot(point=point_2)


        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()
        

        self.add(ax, labels, graph, title, backgroundRectangle1)
        self.play(Create(graph))
        self.add(dot)

        self.play(t.animate.set_value(x_space[minimum_index] + 3.5))
        self.play(t.animate.set_value(x_space[minimum_index] - 3.5))
        self.play(t.animate.set_value(x_space[minimum_index] + 2.5))
        self.play(t.animate.set_value(x_space[minimum_index] - 2.5))
        self.play(t.animate.set_value(x_space[minimum_index] + 1.5))


        self.play(Create(line_1, run_time=1))
        self.play(Create(linear_graph, run_time=1))
        self.play(t.animate.set_value(x_space[minimum_index]), run_time=1)


        self.play(t.animate.set_value(x_space[minimum_index] - 1.5))
        self.play(Create(line_2))
        self.play(Create(linear_graph2))
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait(2)



## now replace parabola for sin with camera movement
class Calculus(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))

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
 
