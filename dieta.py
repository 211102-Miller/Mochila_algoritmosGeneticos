import PyPDF2

archivo_pdf = "datasetalimentos.pdf"

def extraer_texto_pdf(archivo_pdf):
    texto = ""
    with open(archivo_pdf, "rb") as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        for pagina in lector_pdf.pages:
            texto += pagina.extract_text()
    return texto

texto_extraido = extraer_texto_pdf(archivo_pdf)

print("Texto extraído del PDF:")
print(texto_extraido)

