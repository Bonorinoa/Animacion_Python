from manim import *

## Examples with LaTeX
class ejemploLatex(Scene):
    def construct(self):
        
        # titulo
        titulo = Title("Ejemplo LaTex: Demonstración matemática")

        problema = MathTex(r"\text{Si } f(x) = x^k, \text{entonces} f'(x) = k\cdot x^{k-1}", font_size=32).move_to(UP * 2)

        binom = Text("Expansión Binomial:", font_size=24).next_to(problema, DOWN+LEFT)
        mathBinom = MathTex(r"(x+h)^k = x^k + a_1\cdot x^{k-1}\cdot h + ... + a_{k-1}\cdot x\cdot h^{k-1} + a_k\cdot h^k \\", font_size=28).next_to(binom, DR)
        texto0 = MathTex(r"\text{Donde } ", font_size=22).next_to(mathBinom, DL)
        mathBinom2 = MathTex(r"a_j = \frac{k!}{j! \cdot (k-j)!} \forall j = 1...k", font_size=28).next_to(texto0, RIGHT)
        texto1 = MathTex(r"\\ \text{Derivado de la ecuación para combinaciones de probabilidad}", font_size=22).next_to(texto0, DOWN*1.3).to_edge(LEFT)

        paso1 = Text("Aplicando el Teorema Fundamental de Cálculo: ", font_size=18).next_to(texto1, DOWN).to_edge(LEFT)
        TFC = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}", font_size=28).next_to(paso1, RIGHT)

        paso2 = Text("Obtenemos", font_size=16).next_to(TFC, DOWN).to_edge(LEFT)
        paso2b = MathTex(r"\frac{(x+h)^k - x^k}{h} &= \frac{x^k + a_1 \cdot x^{k-1}\cdot h + ... + a_{k-1}\cdot x\cdot h^{k-1} + a_k\cdot h^k - x^k}{h}", font_size=26).next_to(paso2, DR)


        self.add(titulo)
        self.play(Write(problema))
        self.wait(1)
        self.play(Create(binom), Write(mathBinom))
        self.wait(3)
        self.play(Write(texto0), Write(mathBinom2))
        self.play(FadeIn(texto1))
        self.play(Create(paso1), Create(TFC))
        self.wait()
        self.play(Write(paso2), Write(paso2b))

        self.wait(3)

        self.remove(mathBinom, texto0, mathBinom2, texto1, paso1, TFC, paso2)
        self.play(ReplacementTransform(binom, paso2b.next_to(problema, DOWN).to_edge(LEFT)))
        self.wait(2)

        paso3 = MathTex(r"&= \frac{a_1 \cdot x^{k-1}\cdot h + ... + a_{k-1}\cdot x\cdot h^{k-1} + a_k\cdot h^k}{h}" 
        + r"\\ &= \frac{h \cdot (a_1\cdot x^{k-1} + ... + a_k\cdot h^{k-1})}{h}"
        + r"\\ &= a_1\cdot x^{k-1} + ... + a_k\cdot h^{k-1}"
        + r"\\ &= a_1 \cdot x^{k-1} \text{ as } h \rightarrow 0", font_size=26).next_to(paso2b, DOWN)
        self.play(Write(paso3), run_time=6)

        self.wait(2)

        final = MathTex(r"\text{Donde }", font_size=22).next_to(paso3, DL)
        finalb = MathTex(r"a_1 = k. \text{ Entonces, concluimos que } f'(x^k) = k \cdot x^{k-1}.", font_size=26).next_to(final, RIGHT)

        self.play(Write(final), Write(finalb))

        self.wait(2)