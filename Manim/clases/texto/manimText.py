from manim import *

# All animations must reside within the construct() method of a class derived from Scene. 
# Other code, such as auxiliary or mathematical functions, may reside outside the class.
class testCode(Scene):
    def construct(self):
        code = '''from manim import *

class testNums(Scene):
    def construct(self):
        intro = Text("Hello World con Text!", t2c={'[-5:-1]': BLUE})

        self.play(Write(intro))
        self.wait(2)

        introNums = Text("Objetos numericos: ").to_corner(UL)
        decNum = DecimalNumber(3.14159265, num_decimal_places=5)
        integ = Integer(22)
        var = Variable(2.7182818, Text("e"), num_decimal_places=7)

        numbers = [decNum, integ, var]
        nombresNums = Group(Text("DecimalNumber"), Text("Integer"), Text("Variable"))

        for num, name in zip(numbers, nombresNums):
            self.play(Transform(intro, introNums))
            self.play(Write(name.next_to(introNums, RIGHT * 1.5)))
            self.play(Create(num))
            self.wait(3)
            self.play(Unwrite(name), Uncreate(num))

        self.clear()
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", line_spacing=0.5, style="dracula", font="Monospace")

        introCode = Text("Podemos mostrar pedazos de codigo con Code", weight=BOLD).scale(0.75)
        self.play(Write(introCode))
        self.wait(2)
        self.play(ReplacementTransform(introCode, rendered_code.scale(0.7)))
        self.wait(15)

        intro = Text("Hello World con Text!", t2c={'[-5:-1]': BLUE})

        self.play(ReplacementTransform(rendered_code, intro))
        self.wait(2)

        introNums = Text("Objetos numericos: ").to_corner(UL)
        decNum = DecimalNumber(3.14159265, num_decimal_places=5)
        integ = Integer(22)
        var = Variable(2.7182818, Text("e"), num_decimal_places=5)

        numbers = [decNum, integ, var]
        nombresNums = Group(Text("DecimalNumber"), Text("Integer"), Text("Variable"))

        for num, name in zip(numbers, nombresNums):
            self.play(Transform(intro, introNums))
            self.play(Write(name.next_to(introNums, RIGHT * 1.5)))
            self.play(Create(num.scale(4)))
            self.wait(5)
            self.play(Unwrite(name), Uncreate(num))

        self.clear()

        ## TEXTOS (reemplazar por ASCII)

        introTextos = Text("Objetos de texto: ").to_corner(UL)

        text1 = MarkupText(
            f'Todo en rojo <span fgcolor="{YELLOW}">excepto esto</span>', color=RED
        )
        text2 = MarkupText("y esta gradiente de azul a verde", gradient=(BLUE, GREEN))
        text3 = MarkupText(
            'una <gradient from="RED" to="YELLOW">gradiente entre</gradient> otra gradiente',
            gradient=(BLUE, GREEN),
        )
        text4 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        text6 = MarkupText(
            '<span font_family="serif" foreground="blue">mezclar</span> <span font_family="sans">estilos</span> <i>es </i><span font_family="arial"><s>feo</s></span> pero posible'
        )
        text7 = MarkupText("靜我都咕嚕咕嚕", font="sans-serif")

        markupGroup = VGroup(text1, text2, text3, text4, text5, text6, text7).arrange(DOWN)

        parrafo1 = Paragraph("Alguien me pregunto un dia",
                                "Que es un pedo?",
                                "y yo le conteste muy quedo:",
                                "el pedo es un pedo,",
                                "con cuerpo de aire y corazón de viento",
                                "el pedo es como un alma en pena",
                                "que a veces sopla, que a veces truena",
                                "es como el agua que se desliza",
                                "con fuerza y mucha prisa.", line_spacing=1.2, font_size=22, alignment="left").shift(DOWN*0.5)

        parrafo2 = Paragraph("El pedo es como la nube que va volando",
                                "y por donde pasa va fumigando,",
                                "el pedo es vida, el pedo es muerte",
                                "y tiene algo que nos divierte;",
                                "el pedo gime, el pedo llora",
                                "el pedo es aire, el pedo es ruido",
                                "y a veces sale por un descuido",
                                "el pedo es fuerte, es imponente",
                                "pues se los tira toda la gente.", line_spacing=1.2, font_size=22, alignment="left").shift(DOWN*0.5)

        parrafo3 = Paragraph("En este mundo un pedo es vida",
                                "porque hasta el Papa bien se lo tira",
                                "hay pedos cultos e ignorantes",
                                "los hay adultos, también infantes,",
                                "hay pedos gordos, hay pedos flacos,",
                                "según el diámetro de los tacos",
                                "hay pedos tristes,", 
                                "los hay risueños",
                                "según el gusto",
                                "que tiene el dueño", line_spacing=1.2, font_size=22, alignment="left").shift(DOWN*0.5)

        parrafo4 = Paragraph("Si un día algún pedo toca tu puerta",
                                "no se la cierres,",
                                "déjala abierta",
                                "deja que sople", line_spacing=1.2, font_size=26, alignment="left") 
                                                

        self.play(Create(introTextos))
        
        markupNombre = Text("MarkupText").next_to(introTextos, RIGHT * 1.5)
        self.play(Write(markupNombre))
        self.play(FadeIn(markupGroup.scale(0.75)))
        self.wait(25)
        self.play(FadeOut(markupGroup))

        paragNombre = Text("Paragraph").next_to(introTextos, RIGHT * 1.5)
        self.play(ReplacementTransform(markupNombre, paragNombre))
        self.play(GrowFromCenter(parrafo1))
        self.wait(6)
        self.play(ReplacementTransform(parrafo1, parrafo2))
        self.wait(6)
        self.play(ReplacementTransform(parrafo2, parrafo3))
        self.wait(6)
        self.play(Uncreate(parrafo3), Write(parrafo4))
        self.wait(6)

