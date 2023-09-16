import sys

def verificar_lista(participantes):
    longitud_referencia = len(participantes[0][1])

    if not all(len(un_participante[1]) == longitud_referencia for un_participante in participantes):
        print("Todos los participantes deben tener la misma cantidad de categorías")
        return False

    if not all(all(1 <= categoria <= longitud_referencia for categoria in un_participante[1]) for un_participante in participantes):
        print("Hay participantes con código erróneo de categoría")
        return False

    return True

def leer_participantes(nombre_archivo):
    participantes = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.split(",", 1)
                participantes.append([datos[0], [ int(x) for x in datos[1].split(",") ]])

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
    
    return participantes

def obtener_posicion(participantes, pos_string):
    try:
        pos_capitan = int(pos_string)
    except ValueError:
        print("Número de capitán inválido")
        return
        
    if (pos_capitan <= 0 or pos_capitan > len(participantes)):
        print("Número de capitán inválido")
        return -1
    
    return pos_capitan - 1

def main():
    if len(sys.argv) != 3:
        print("Uso: python contest.py participantes.txt 4")
        return

    archivo_participantes = sys.argv[1]
    participantes = leer_participantes(archivo_participantes)
    print(participantes)
    
    if (not verificar_lista(participantes)):
        return
    
    pos_capitan = obtener_posicion(participantes, sys.argv[2])
    
    if pos_capitan < 0: 
        return
        
    print(participantes[pos_capitan])


if __name__ == "__main__":
    main()