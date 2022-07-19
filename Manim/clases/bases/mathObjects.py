from manim import *

# NOTES: Add some linear algebra examples
# A few advanced camera settings and background color change

## Display all MObjects available
class firstMObjects(ThreeDScene):
    def construct(self):
        some2DMobjects = Group(Circle(), Triangle(), Square(),
                     Star(), Star().round_corners(radius=0.5),
                     RegularPolygon(n=10, color=RED),
                     DecimalMatrix(
                        [[3.456, 2.122], [33.2244, 12]],
                        element_to_mobject_config={"num_decimal_places": 2},
                        left_bracket="\{",
                        right_bracket="\}"),
                     MathTable(
                        [["+", 0, 5, 10],
                        [0, 0, 5, 10],
                        [2, 2, 7, 12],
                        [4, 4, 9, 14]],
                        include_outer_lines=True)).scale(0.75)
        
        positions = [UL, UR, DL, DR, UP, DOWN, LEFT, RIGHT]

        for pos, mobject in zip(positions, some2DMobjects):
            self.play(FadeIn(mobject))
            self.play(mobject.animate.move_to(pos*3))
        
        self.wait(2)

        self.clear()

        texto0 = Text("Pero 2D lo maneja cualquiera...")
        self.play(Write(texto0), run_time=3)
        self.play(Uncreate(texto0))
        self.wait(2)

        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]

        some3DMobjects = Group(Dodecahedron(), Icosahedron(),
                          Polyhedron(vertex_coords, faces_list),
                          Octahedron(edge_length = 2).faces[2:3].set_color(YELLOW)).scale(0.75)

        positions = [UL, UR, DL, DR]

        for pos, mobject in zip(positions, some3DMobjects):
            self.play(FadeIn(mobject))
            self.play(mobject.animate.move_to(pos*3))
        
        self.wait(2)
        
        text3d = Text("Bienvenidos a la 3ra dimension", color=ORANGE)
        self.play(Write(text3d), run_time=2)
        self.play(Unwrite(text3d), run_time=3)

        ## MObjects in 3D
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(ThreeDAxes())

        self.wait(3)

        self.move_camera(phi=360 * DEGREES, theta=270 * DEGREES)

        self.wait(3)

        self.clear()

        texto = Text("Y? Que les parece?")
        self.play(FadeIn(texto), run_time=2)
        self.play(FadeOut(texto))
        self.wait(1)

        texto2 = Text("Bastante bueno no? Es lo minimo que podemos crear...", font_size=30)
        self.play(ReplacementTransform(texto, texto2))
        self.play(Circumscribe(texto2[20:26], fade_out=True, run_time=4))
        self.wait(1)
        self.play(FadeOut(texto2))

        texto3 = Text("Solo se pone mas entretenido desde aca")
        self.play(SpiralIn(texto3))
        self.play(ApplyWave(texto3, rate_func=linear, ripples=4))
        self.wait(1)
        self.play(Unwrite(texto3))
        self.wait(2)