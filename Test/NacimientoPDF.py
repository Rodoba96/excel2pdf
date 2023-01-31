# Import Dependencies
import pandas as pd
import numpy as np
from fpdf import FPDF
import unicodedata

# Reading input files
#path = r'C:\Desktop\Football Clubs\England\Premier League'
Input_path = "CatalogoNAC_02.xlsx"
df = pd.read_excel(Input_path, sheet_name='Inventario')
#print(df)

# def unicode_normalize(s):
#     return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    #return unicodedata('NFKD', s).encode('ascii', 'ignore')

# Creating variables
n = 0
numero = df["Num."].iloc[n]
pais = df["Pais"].iloc[n]
ciudad = df["Ciudad"].iloc[n]
descripción = df["Descripcion"].iloc[n]
material = df["Material"].iloc[n]
regalo = df["Regalo de:"].iloc[n]
piezas = df["Piezas"].iloc[n]
año = df["Ano"].iloc[n]

# PDF creation
pdf = FPDF("P", "mm", "A4") # Initializing object
pdf.add_page() # Adding new page
pdf.set_font('arial', size=12)


# Box of image
pdf.set_xy(12,64)
pdf.cell(0, 100, txt='Insert image', border=True, ln=1, align="C",fill=False)

# Text box for number
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=9, style="B")
pdf.set_xy(12,76)
#pdf.multi_cell(120, 5, txt= unicode_normalize(numero), align="J")
pdf.multi_cell(120, 5, txt= numero, align="J")

# # Text box 
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=9, style="B")
pdf.set_xy(12,165)
pdf.multi_cell(180, 5, txt= pais, align="J")

# # Text box 
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=9, style="B")
pdf.set_xy(12,165)
pdf.multi_cell(180, 5, txt= ciudad, align="J")

# Exporting PDF
pdf.output("CatalogoPDF.pdf")