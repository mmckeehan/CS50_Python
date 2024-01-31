from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        self._pdf = FPDF(orientation="portrait")
        self._name = name

        self._pdf.add_page()
        self.header()
        self._pdf.ln(30)
        self.shirt()
        self._pdf.output("shirtificate.pdf")


    def header(self):
        title = "CS50 Shirtificate"
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.ln(30)
        self._pdf.cell(1, 10, title, align="C", center = True)

    def shirt(self):
        _text = f"{self._name} took CS50"
        width = self._pdf.get_string_width(_text)
        shirt_w = (210 - 150) / 2

        self._pdf.image("shirtificate.png", w= 150, h= 150, x= shirt_w)
        self._pdf.set_font("helvetica", "B", 15)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_x((210 - width) / 2)
        self._pdf.set_y((297 / 2) - 30)
        self._pdf.cell(width, 10, _text, align="C", center = True)



name = input("Name: ")
pdf = PDF(name)
