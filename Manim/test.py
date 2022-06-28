import itertools as it
from manim import *
from numpy.lib.function_base import iterable

# A customizable Sequential Neural Network


class NeuralNetworkMobject(VGroup):
    # Remove CONFIG since it is now deprecated in ManimCE
    # CONFIG = {
    #     "neuron_radius": 0.15,
    #     "neuron_to_neuron_buff": MED_SMALL_BUFF,
    #     "layer_to_layer_buff": LARGE_BUFF,
    #     "output_neuron_color": WHITE,
    #     "input_neuron_color": WHITE,
    #     "hidden_layer_neuron_color": WHITE,
    #     "neuron_stroke_width": 2,
    #     "neuron_fill_color": GREEN,
    #     "edge_color": LIGHT_GREY,
    #     "edge_stroke_width": 2,
    #     "edge_propogation_color": YELLOW,
    #     "edge_propogation_time": 1,
    #     "max_shown_neurons": 16,
    #     "brace_for_large_layers": True,
    #     "average_shown_activation_of_large_layer": True,
    #     "include_output_labels": False,
    #     "arrow": False,
    #     "arrow_tip_size": 0.1,
    #     "left_size": 1,
    #     "neuron_fill_opacity": 1
    # }

    # Constructor with parameters of the neurons in a list
    def __init__(
        self,
        neural_network,
        *args,

            neuron_radius=0.16,
            neuron_to_neuron_buff=MED_SMALL_BUFF,
            layer_to_layer_buff=LARGE_BUFF,
            output_neuron_color=YELLOW,
            input_neuron_color=BLUE,
            hidden_layer_neuron_color=GREEN,
            neuron_stroke_width=2,
            neuron_fill_color=GREEN,
            edge_color=LIGHT_GREY,
            edge_stroke_width=2,
            edge_propogation_color=YELLOW,
            edge_propogation_time=1,
            max_shown_neurons=12,
            brace_for_large_layers=True,
            average_shown_activation_of_large_layer=True,
            include_output_labels=False,
            arrow=False,
            arrow_tip_size=0.1,
            left_size=1,
            neuron_fill_opacity=1,

            **kwargs,
    ):
        VGroup.__init__(self, *args, **kwargs)

        self.neuron_radius = neuron_radius
        self.neuron_to_neuron_buff = neuron_to_neuron_buff
        self.layer_to_layer_buff = layer_to_layer_buff
        self.output_neuron_color = output_neuron_color
        self.input_neuron_color = input_neuron_color
        self.hidden_layer_neuron_color = hidden_layer_neuron_color
        self.neuron_stroke_width = neuron_stroke_width
        self.neuron_fill_color = neuron_fill_color
        self.edge_color = edge_color
        self.edge_stroke_width = edge_stroke_width
        self.edge_propogation_color = edge_propogation_color
        self.edge_propogation_time = edge_propogation_time
        self.max_shown_neurons = max_shown_neurons
        self.brace_for_large_layers = brace_for_large_layers
        self.average_shown_activation_of_large_layer = average_shown_activation_of_large_layer
        self.include_output_labels = include_output_labels
        self.arrow = arrow
        self.arrow_tip_size = arrow_tip_size,
        self.left_size = left_size
        self.neuron_fill_opacity = neuron_fill_opacity

        self.layer_sizes = neural_network
        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)

    # Helper method for constructor
    def add_neurons(self):
        layers = VGroup(*[
            self.get_layer(size, index)
            for index, size in enumerate(self.layer_sizes)
        ])
        layers.arrange_submobjects(RIGHT, buff=self.layer_to_layer_buff)
        self.layers = layers
        if self.include_output_labels:
            self.label_outputs_text()
    # Helper method for constructor

    def get_nn_fill_color(self, index):
        if index == -1 or index == len(self.layer_sizes) - 1:
            return self.output_neuron_color
        if index == 0:
            return self.input_neuron_color
        else:
            return self.hidden_layer_neuron_color
    # Helper method for constructor

    def get_layer(self, size, index=-1):
        layer = VGroup()
        n_neurons = size
        if n_neurons > self.max_shown_neurons:
            n_neurons = self.max_shown_neurons
        neurons = VGroup(*[
            Circle(
                radius=self.neuron_radius,
                stroke_color=self.get_nn_fill_color(index),
                stroke_width=self.neuron_stroke_width,
                fill_color=BLACK,
                fill_opacity=self.neuron_fill_opacity,
            )
            for x in range(n_neurons)
        ])
        neurons.arrange_submobjects(
            DOWN, buff=self.neuron_to_neuron_buff
        )
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = Tex("\\vdots")
            dots.move_to(neurons)
            VGroup(*neurons[:len(neurons) // 2]).next_to(
                dots, UP, MED_SMALL_BUFF
            )
            VGroup(*neurons[len(neurons) // 2:]).next_to(
                dots, DOWN, MED_SMALL_BUFF
            )
            layer.dots = dots
            layer.add(dots)
            if self.brace_for_large_layers:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer
    # Helper method for constructor

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)
    # Helper method for constructor

    def get_edge(self, neuron1, neuron2):
        if self.arrow:
            return Arrow(
                neuron1.get_center(),
                neuron2.get_center(),
                buff=self.neuron_radius,
                stroke_color=self.edge_color,
                stroke_width=self.edge_stroke_width,
                tip_length=self.arrow_tip_size
            )
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=self.neuron_radius,
            stroke_color=self.edge_color,
            stroke_width=self.edge_stroke_width,
        )

    # Labels each input neuron with a char l or a LaTeX character
    def label_inputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[0].neurons):
            label = MathTex(f"{l}_"+"{"+f"{n + 1}"+"}")
            label.height = (0.3 * neuron.height)
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels each output neuron with a char l or a LaTeX character
    def label_outputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = MathTex(f"{l}_"+"{"+f"{n + 1}"+"}")
            label.height = (0.4 * neuron.height)
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels each neuron in the output layer with text according to an output list
    def label_outputs_text(self, outputs):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = MathTex(outputs[n])
            label.height = (0.75*neuron.height)
            label.move_to(neuron)
            label.shift((neuron.width + label.width/2)*RIGHT)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels the hidden layers with a char l or a LaTeX character
    def label_hidden_layers(self, l):
        self.output_labels = VGroup()
        for layer in self.layers[1:-1]:
            for n, neuron in enumerate(layer.neurons):
                label = MathTex(f"{l}_{n + 1}")
                label.height = (0.4 * neuron.height)
                label.move_to(neuron)
                self.output_labels.add(label)
        self.add(self.output_labels)



class myNeuralNetwork(Scene):
    def construct(self):
        myNetwork = NeuralNetworkMobject([15, 5, 2])

        myNetwork.label_inputs('x')
        myNetwork.label_outputs('\hat{y}')
        myNetwork.label_hidden_layers('a')
        myNetwork.label_outputs_text(['Clase 1', 'Clase 2'])

        texto = MarkupText("Red Neuronal \n Clasificacion Multiple", font_size=30).to_corner(UL)
        self.play(Write(texto), Write(myNetwork), run_time=7)
        self.play(Circumscribe(texto))
        self.wait(1)

#---------------------
#---------------------
#---------------------


#               _                 _       
#    __ _ _ __ (_)_ __ ___   __ _| |_ ___ 
#   / _` | '_ \| | '_ ` _ \ / _` | __/ _ \
#  | (_| | | | | | | | | | | (_| | ||  __/
# (_)__,_|_| |_|_|_| |_| |_|\__,_|\__\___|

class AnimateMethod(Scene):
    def construct(self):
        sq = Square()
        sq.save_state()
        self.add(sq)

        # New form
        self.play(
            sq.animate.to_edge(DOWN,buff=1)
        )
        self.wait()

        self.play(Restore(sq))
        self.wait()
        # Old form still works
        self.play(
            sq.to_edge,DOWN,{"buff": 1}
        )
        self.wait()

        # Multiple methods
        self.play(
            sq.animate
                .scale(2)
                .set_color(ORANGE)
                .to_corner(UR,buff=1)
        )
        self.wait()
        
#  _           _       _         _            
# (_)___  ___ | | __ _| |_ ___  | |_ _____  __
# | / __|/ _ \| |/ _` | __/ _ \ | __/ _ \ \/ /
# | \__ \ (_) | | (_| | ||  __/ | ||  __/>  < 
# |_|___/\___/|_|\__,_|\__\___|  \__\___/_/\_\


#class IsolateTex1(Scene):  # THIS IS DEPRECATED, use isolate instead
    # def construct(self):
        #t1 = Tex("{{x}}")
        #t2 = Tex("{{x}} - {{x}}")
        #VGroup(t1,t2)\
        #    .scale(3)\
        #    .arrange(DOWN)

        #self.add(t1)
        #self.wait()
        #self.play(
        #    TransformMatchingTex(t1,t2),
        #    run_time=4
        #)
        #self.wait()


class IsolateTex1v2(Scene):
    def construct(self):
        isolate_tex = ["x"]
        t1 = Tex("x",isolate=isolate_tex)
        t2 = Tex("x - x",isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(t1,t2),
            run_time=4
        )
        self.wait()


class IsolateTex1v3(Scene):
    def construct(self):
        t1 = Tex("x")
        t2 = Tex("x - x")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            # If the formula is complex this animation will not work.
            TransformMatchingShapes(t1,t2),
            run_time=4
        )
        self.wait()


class IsolateTex2(Scene):
    def construct(self):
        isolate_tex = ["x","y","3","="]
        t1 = Tex("x+y=3",isolate=isolate_tex)
        t2 = Tex("x=3-y",isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)
        t2.align_to(t1,LEFT)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2,
                # Try removing this dictionary
                key_map={
                    "+":"-"
                }
            ),
            run_time=4
        )
        self.wait()

class IsolateTex3(Scene):
    def construct(self):
        isolate_tex = ["a","b","c","="]
        t1 = Tex("a\\times b = c",isolate=isolate_tex)
        t2 = Tex("a = { c \\over b }",isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)
        t2.align_to(t1,LEFT)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2,
                key_map={
                    "\\times":"\\over"
                }
            ),
            run_time=4
        )
        self.wait()


#  _____         _     _____                     __
# |  ___|_ _  __| | __|_   _| __ __ _ _ __  ___ / _| ___  _ __ _ __ ___  
# | |_ / _` |/ _` |/ _ \| || '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \ 
# |  _| (_| | (_| |  __/| || | | (_| | | | \__ \  _| (_) | |  | | | | | |
# |_|  \__,_|\__,_|\___||_||_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_|


class FadeTransformExample(Scene):
    def construct(self):
        m1 = Text("Hello world").to_corner(UL)
        m2 = Text("I'm FadeTransform").to_corner(DR)

        self.add(m1)
        self.wait()
        self.play(
            # Equivalent to ReplacementTransform
            FadeTransform(m1,m2),
            run_time=4
        )


class ExtrangeTransform(Scene):
    def construct(self):
        t1 = Tex("e^","\\frac{-it\\pi}{\\omega}")
        t2 = Tex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN,buff=2)
            
        self.add(t1,t2.copy().fade(0.8))
        self.wait()
        self.play(
            TransformFromCopy(t1[-1],t2[0]),
            run_time=6
        )
        self.wait()

class ExtrangeTransformFixed(Scene):
    def construct(self):
        t1 = Tex("e^","\\frac{-it\\pi}{\\omega}")
        t2 = Tex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN,buff=2)
            
        self.add(t1,t2.copy().fade(0.8))
        self.wait()
        self.play(
            FadeTransformPieces(t1[-1].copy(),t2[0]),
            run_time=4
        )
        self.wait()


#   ____                 _     ____
#  / ___|_ __ __ _ _ __ | |__ / ___|  ___ ___ _ __   ___ 
# | |  _| '__/ _` | '_ \| '_ \\___ \ / __/ _ \ '_ \ / _ \
# | |_| | | | (_| | |_) | | | |___) | (_|  __/ | | |  __/
#  \____|_|  \__,_| .__/|_| |_|____/ \___\___|_| |_|\___|
#                 |_|                                    

class AxesExample(Scene):
    def construct(self):
        X_MIN = -5
        X_MAX = 5
        # You can have multiple Axes
        axes_config = {
            # [min, max, step]
            "x_range": [X_MIN,X_MAX,0.5],
            "y_range": [-3,3,1],
            "height": FRAME_HEIGHT - 2,
            "width": FRAME_WIDTH - 2,
            "axis_config": {
                "include_tip": True,
                "numbers_to_exclude": [0],
            },
            "x_axis_config": {
                # see manimlib/mobjects/number_line.py
                "line_to_number_buff": 0.5,
                "line_to_number_direction": UP,
                "color": RED
            },
            "y_axis_config": {
                "decimal_number_config": {
                    # see manimlib/mobjects/numbers.py
                    "num_decimal_places": 1,
                },
            },
        }
        axes = Axes(**axes_config)
        axes.add_coordinate_labels(font_size=20)
        graph = axes.get_graph(
            lambda x: np.sin(x),
            x_min=X_MIN,
            x_max=X_MAX
        )
        
        self.add(axes,graph)

#  _____ _                   ____  ____
# |_   _| |__  _ __ ___  ___|  _ \/ ___|  ___ ___ _ __   ___ 
#   | | | '_ \| '__/ _ \/ _ \ | | \___ \ / __/ _ \ '_ \ / _ \
#   | | | | | | | |  __/  __/ |_| |___) | (_|  __/ | | |  __/
#   |_| |_| |_|_|  \___|\___|____/|____/ \___\___|_| |_|\___|


# New 3D mobjects
class Sphere(Surface):
    CONFIG = {
        "radius": 1,
        "u_range": (0, TAU),
        "v_range": (0, PI),
    }

    def uv_func(self, u, v):
        return self.radius * np.array([
            np.cos(u) * np.sin(v),
            np.sin(u) * np.sin(v),
            -np.cos(v)
        ])


class Torus(Surface):
    CONFIG = {
        "u_range": (0, TAU),
        "v_range": (0, TAU),
        "r1": 3,
        "r2": 1,
    }

    def uv_func(self, u, v):
        P = np.array([math.cos(u), math.sin(u), 0])
        return (self.r1 - self.r2 * math.cos(v)) * P - math.sin(v) * OUT



class ThreeDSceneExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)

        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        torus2.mesh = SurfaceMesh(torus2)
        sphere.mesh = SurfaceMesh(sphere)
        
        surface = sphere
        surface.save_state()
        self.play(
            ShowCreation(surface)
        )
        self.wait()
        self.play(
            Transform(surface,torus1)
        )
        self.wait()
        self.play(
            Transform(surface,torus2)
        )
        self.wait()
        
        
        self.play(Write(torus2.mesh))
        self.wait()
        
        self.play(
            Restore(surface),
            ReplacementTransform(
                torus2.mesh,
                sphere.mesh
            )
        )
        self.wait()

""" 
class ThreeDScene(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def setup(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.frame = frame """

class Functions3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        para_hyp = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**3-v**4
            ]),
            v_range=(-2,2),
            u_range=(-2,2),
            fill_opacity =0.5,
            fill_color=RED,
            resolution=(15, 32)
        )

        #(a - b) cos t + c cos ((a/b - 1)t)

        func = MathTex(r"z=x^3-y^4").to_corner(DL)
        self.add_fixed_in_frame_mobjects(func)

        self.play(Create(axes))
        
        self.play(
            Create(para_hyp)
        )

        # Set perspective
        theta_tracker = ValueTracker(75)
        self.move_camera(phi=10 * DEGREES, theta=60 * DEGREES)
        # Add ambient rotation
        #self.add_updater(lambda m, dt: m.set_theta(m.get_theta() - (0.1 * dt)))

        self.play(Write(func), theta_tracker.animate.increment_value(140))
        self.wait(2)

        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3 * IN).scale(1.5), run_time=2)
        self.play(light.animate.shift(10 * OUT).scale(1.5), run_time=2)
        self.wait(2)

        self.play(Restore(light))


