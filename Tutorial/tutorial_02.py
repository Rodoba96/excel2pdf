from fpdf import FPDF
from fpdf.enums import XPos, YPos


class PDF(FPDF):
    def header(self):
        # Logo
        #self.image(name='logo_pb.png', x=10, y=8, w=33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        #self.cell(w=0, h=10, txt='Page ' + str(self.page_no()) + '/{nb}', border=1, ln=0, center='C')
        self.cell(w=0, h=10, txt='Page' + str(self.page_no()) + '/{nb}', border=1, new_x=XPos.RIGHT, new_y=YPos.NEXT, center="C")

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
for i in range(1, 41):
    pdf.cell(0, 10, 'Printing line number ' + str(i), 1, 1)
pdf.output('tuto2.pdf', 'F')