#esto solo se encargara de encontrar los PDFs disponibles y permitir seleccionar uno

from pathlib import Path

PDF_DIR=Path("pdfs")

#Funcion para solo encontrar pdfs
def find_pdfs():
    if not PDF_DIR.exists():
        return []

    return [file for file in PDF_DIR.iterdir() if file.is_file() and file.suffix.lower()==".pdf"]