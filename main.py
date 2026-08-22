from scanner.discovery import find_pdfs
from scanner.javascript import analyze_javascript

# Obtiene la lista de PDFs encontrados en la carpeta
pdfs=find_pdfs()

if not pdfs:
    print("No se encontraron archivos PDF.")
    exit()

for i,pdf in enumerate(pdfs,1):
    print(f"[{i}] {pdf.name}")

# Convierte la selección del usuario en el índice del PDF elegido
selection=int(input("Selecciona un PDF: "))
pdf=pdfs[selection-1]

print(f"\nAnalizando: {pdf.name}")

# Ejecuta el análisis y guarda los indicadores encontrados
found=analyze_javascript(pdf)

print("\nAnálisis de JavaScript")

if found:
    print("[!] Indicadores encontrados:")
    for indicator in found:
        print(f"    {indicator}")
else:
    print("[OK] No se encontraron indicadores.")