from pathlib import Path

INDICATORS=[b"/JavaScript",b"/JS"]

def analyze_javascript(pdf_path):
    #Realmente no leemos el pdf como texto sino como Bytes para buscar secuencias
    data=Path(pdf_path).read_bytes()
    found=[]

    for indicator in INDICATORS:
        if indicator in data:
            found.append(indicator.decode())

    return found

#Internamente Python puede recibir algo como b'%PDF-1.7\n1 0 obj\n<< /Type...'
#La "b" significa que buscamos una secuencia de bytes, no un str normal de python.