from manim import *

class transfVSreplacement(Scene):
    def construct(self):

        mobject = Text("A", color=RED).shift(LEFT)
        mobjectTarget = Text("B", color=BLUE)
        mobjectTarget2 = Text("C", color=ORANGE).shift(RIGHT)

        transform = Text("Transform", weight=BOLD).shift(UP)

        self.play(Write(transform), Create(mobject), Create(mobjectTarget), Create(mobjectTarget2))

        self.wait(3)

        self.play(Transform(mobject, mobjectTarget), run_time=5)

        self.wait(2)

        self.play(Transform(mobjectTarget, mobjectTarget2), run_time=5)

        self.wait(2)

        self.clear()

        repmobject = Text("A", color=RED).shift(LEFT)
        repmobjectTarget = Text("B", color=BLUE)
        repmobjectTarget2 = Text("C", color=ORANGE).shift(RIGHT)

        reptransform = Text("Replacement Transform", weight=BOLD).shift(UP)

        self.wait(2)

        self.play(Write(reptransform), Create(repmobject), Create(repmobjectTarget), Create(repmobjectTarget2))

        self.wait(3)

        self.play(ReplacementTransform(repmobject, repmobjectTarget), run_time=5)

        self.wait(2)

        self.play(ReplacementTransform(repmobjectTarget, repmobjectTarget2), run_time=5)

        self.wait(2)

class textoCodigo(Scene):
    def construct(self):

        code = '''from manim import *
#Transform
mobject = Text("A", color=RED).shift(LEFT)
mobjectTarget = Text("B", color=BLUE)
mobjectTarget2 = Text("C", color=ORANGE).shift(RIGHT)

transform = Text("Transform", weight=BOLD).shift(UP)

self.play(Write(transform), Create(mobject), Create(mobjectTarget), Create(mobjectTarget2))

self.play(Transform(mobject, mobjectTarget), run_time=5)

self.play(Transform(mobjectTarget, mobjectTarget2), run_time=5)

self.clear()

# ReplacementTransform
repmobject = Text("A", color=RED).shift(LEFT)
repmobjectTarget = Text("B", color=BLUE)
repmobjectTarget2 = Text("C", color=ORANGE).shift(RIGHT)

reptransform = Text("Replacement Transform", weight=BOLD).shift(UP)

self.play(Write(reptransform), Create(repmobject), Create(repmobjectTarget), Create(repmobjectTarget2))

self.play(ReplacementTransform(repmobject, repmobjectTarget), run_time=5)

self.play(ReplacementTransform(repmobjectTarget, repmobjectTarget2), run_time=5)
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", line_spacing=0.5, style="dracula", font="Monospace")
        self.add(rendered_code.scale(0.55))