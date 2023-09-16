import sys

def leer_habilidades(nombre_archivo):
    habilidades = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                habilidades.append(linea.split(",")[1].strip())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
    
    return habilidades

def leer_candidatos(nombre_archivo):
    candidatos = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.split(",", 1)
                candidatos[datos[0]] = [ int(x) for x in datos[1].split(",") ]
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
    
    return candidatos

def main():
    if len(sys.argv) != 3:
        print("Uso: python antarctic_base.py habilidades.txt candidatos.txt")
        return

    archivo_habilidades = sys.argv[1]
    archivo_candidatos = sys.argv[2]

    habilidades = leer_habilidades(archivo_habilidades)
    candidatos = leer_candidatos(archivo_candidatos)
    print(candidatos)
    habilidades_cubiertas = [0] * len(habilidades)

if __name__ == "__main__":
    main()