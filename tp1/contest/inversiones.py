from contest_utils import leer_participantes, crear_diccionario_capitan;

cantidad_inversiones = 0

def calcular_inversiones(lista_categoria_izq, lista_categoria_der, categorias_capitan):
    categorias_final = []
    global cantidad_inversiones 
    #categorias_lado_derecho = len(lista_categoria_der)
    
    while (len(lista_categoria_izq) > 0) and (len(lista_categoria_der) > 0):
        categoria_izq = lista_categoria_izq[0]
        categoria_der = lista_categoria_der[0]
        
        if categorias_capitan[categoria_izq] < categorias_capitan[categoria_der]:
            categorias_final.append(lista_categoria_izq.pop(0))
        else:
            categorias_final.append(lista_categoria_der.pop(0))
            cantidad_inversiones += len(lista_categoria_izq)
    
    #cantidad_inversiones += categorias_lado_derecho * len(lista_categoria_izq)
    
    if (len(lista_categoria_izq) > 0):
        categorias_final += lista_categoria_izq
    
    if (len(lista_categoria_der) > 0):
        categorias_final += lista_categoria_der
        
    return categorias_final

def contar_inversiones(lista_categorias, categorias_capitan):
    longitud_categorias = len(lista_categorias)
    
    if longitud_categorias == 1: return lista_categorias
    
    mitad = longitud_categorias // 2
    parte_izquierda = lista_categorias[:mitad]
    parte_derecha = lista_categorias[mitad:]
    
    return calcular_inversiones(
        contar_inversiones(parte_izquierda, categorias_capitan),
        contar_inversiones(parte_derecha, categorias_capitan),
        categorias_capitan
    )

def main():
    #lista = [1, 2, 3, 4, 5]
    lista = [1, 9, 6, 4, 5]
    #lista = [8, 1, 7, 2, 6, 3, 5, 4]
    global cantidad_inversiones
    
    diccionario = crear_diccionario_capitan(lista)
    
    a = contar_inversiones(lista, diccionario)
    print(f"{a} en {cantidad_inversiones}")
    
    cantidad_inversiones = 0
    lista_b = lista[::-1]
    #lista_b = [1, 4, 9, 6, 5]
    print(f"{lista} - {lista_b}")
    b = contar_inversiones(lista_b, diccionario)
    print(f"{b} en {cantidad_inversiones}")
    
    return 0
    
if __name__ == "__main__":
    main()