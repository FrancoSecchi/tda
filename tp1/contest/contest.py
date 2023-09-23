import sys
from contest_utils import leer_participantes, crear_diccionario_capitan;
from investment_counting import obtener_cantidad_inversiones;

def main():
    if len(sys.argv) != 3:
        print("Uso: python contest.py participantes.txt 4")
        return

    archivo_participantes = sys.argv[1]
    pos_capitan = sys.argv[2]
    participantes, capitan = leer_participantes(archivo_participantes, pos_capitan)
    
    if capitan is None:
        print("Número de capitán inválido")
        return
    
    categorias_capitan = crear_diccionario_capitan(capitan['categorias'])
    
    nombre_companiero = ""
    max_inversiones = -1
    
    for un_participante in participantes:
        inversiones_participantes = obtener_cantidad_inversiones(un_participante[1], categorias_capitan)
        if inversiones_participantes > max_inversiones:
            max_inversiones = inversiones_participantes
            nombre_companiero = un_participante[0]
            
    print(f"{capitan['nombre']}, {nombre_companiero}")
    
if __name__ == "__main__":
    main()