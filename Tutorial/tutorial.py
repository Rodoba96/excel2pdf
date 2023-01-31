# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html

from fpdf import FPDF

#     portraid, millimeters, page type
#pdf = FPDF('P', 'mm', 'A4')
pdf = FPDF()
pdf.add_page() # Adding new page
pdf.set_font(family='Arial', style='B', size=16) # Setting the font: Arial, Bold, size
pdf.cell(w=40, h=10, txt='Hello World!', border=1)
pdf.cell(w=60, h=10, txt='Powered by FPDF.', border=1, ln=1, align='C', center='C')
pdf.output('tuto1.pdf', 'F')