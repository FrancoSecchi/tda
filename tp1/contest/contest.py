import sys
from contest_utils import leer_participantes, crear_diccionario_capitan;

def main():
    if len(sys.argv) != 3:
        print("Uso: python contest.py participantes.txt 4")
        return

    archivo_participantes = sys.argv[1]
    pos_capitan = sys.argv[2]
    datos_iniciales = leer_participantes(archivo_participantes, pos_capitan)
    
    participantes = datos_iniciales['participantes']
    capitan = datos_iniciales['capitan']
    
    print(participantes)
    print(capitan)
    
    if capitan is None:
        print("Número de capitán inválido")
        return
    
    dic_capitan = crear_diccionario_capitan(capitan['categorias'])
    print(dic_capitan)
    
if __name__ == "__main__":
    main()