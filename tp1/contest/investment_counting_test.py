from contest_utils import crear_diccionario_capitan;
from investment_counting import obtener_cantidad_inversiones;

def main():
    listado = [
        [2,6,1,4,3,5,7,8],
        [1,3,5,4,8,2,6,7],
        [7,8,2,1,4,3,5,6],
        [8,1,5,7,2,6,3,4],
        [8,1,7,2,5,3,4,6]        
    ]
    
    len_listado = len(listado)
    for i in range(len_listado):
        print(f"Calculando inversiones con N°{i + 1} {listado[i]}")
        dic_listado_i = crear_diccionario_capitan(listado[i])
        for j in range(i + 1, len_listado):
            print(f"\t- N°{j + 1} {listado[j]}: total de {obtener_cantidad_inversiones(listado[j], dic_listado_i)}")    

if __name__ == "__main__":
    main()
