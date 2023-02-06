# Import Dependencies
import pandas as pd
import numpy as np
from fpdf import FPDF
import unicodedata

# Reading input files
# Input_path = "CatalogoNAC_02.xlsx"
# df = pd.read_excel(Input_path, sheet_name='Inventario')
#print(df)

title = 'Nacimientos'

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial','B',15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)  # Blue
        self.set_fill_color(255, 255, 255) # Yellow
        self.set_text_color(0, 0, 0) # Black
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w=w, h=9, txt=title, border=1, ln=1, align='C', fill=1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def nacimiento_num(self, num):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Número: %d' % (num), 0, 1, 'L', 1)
        # Line break
        self.ln(0)
    
    def nacimiento_pais(self, pais):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'País: %s' % (pais), 0, 1, 'L', 1)
        # Line break
        self.ln(0)

    def nacimiento_ciudad(self, ciudad):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Ciudad: %s' % (ciudad), 0, 1, 'L', 1)
        # Line break
        self.ln(0)

    def nacimiento_descripcion(self, descripcion):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Descripción: %s' % (descripcion), 0, 1, 'L', 1)
        # Line break
        self.ln(0)

    def nacimiento_material(self, material):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Material: %s' % (material), 0, 1, 'L', 1)
        # Line break
        self.ln(0)
    
    def nacimiento_regalo(self, regalo):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Regalo de: %s' % (regalo), 0, 1, 'L', 1)
        # Line break
        self.ln(0)
    
    def nacimiento_piezas(self, piezas):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Piezas: %d' % (piezas), 0, 1, 'L', 1)
        # Line break
        self.ln(0)

    def nacimiento_year(self, year):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Año: %d' % (year), 0, 1, 'L', 1)
        # Line break
        self.ln(0)

    def nacimiento_image(self):
        self.ln(6)
        self.cell(0, 190,'', 1,1)
        self.ln(0)    

    def print_nacimiento(self, num, pais, ciudad, descripcion, material, regalo, piezas, year):
        self.add_page()
        self.nacimiento_num(num)
        self.nacimiento_pais(pais)
        self.nacimiento_ciudad(ciudad)
        self.nacimiento_descripcion(descripcion)
        self.nacimiento_material(material)
        self.nacimiento_regalo(regalo)
        self.nacimiento_piezas(piezas)
        self.nacimiento_year(year)
        self.nacimiento_image()

pdf = PDF()
pdf.set_title(title)
pdf.print_nacimiento(1, 'México', 'CDMX', '1er . Nacimiento.', 'Pasta', 'Tía Silvia', 15, 1990)
pdf.print_nacimiento(2, 'México', 'Apaseo el Grande, GTO.', '', 'Tallado de madera', '', 10, 1995)
pdf.print_nacimiento(3, 'México', '', 'Nacimiento grande de Costco', 'Porcelana', '', 3, 1998)
pdf.output('tuto3.pdf', 'F')

