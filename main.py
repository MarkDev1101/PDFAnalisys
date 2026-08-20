from scanner.discovery import find_pdfs

pdfs = find_pdfs()

for pdf in pdfs:
    print(pdf)