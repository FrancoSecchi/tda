from contest_utils import leer_participantes, crear_diccionario_capitan;

def calcular_inversiones(lista_categoria_izq, lista_categoria_der, categorias_capitan):
    categorias_final = []
    cantidad_inversiones = 0 
    #categorias_lado_derecho = len(lista_categoria_der)
    
    while (len(lista_categoria_izq) > 0) and (len(lista_categoria_der) > 0):
        categoria_izq = lista_categoria_izq[0]
        categoria_der = lista_categoria_der[0]
        
        if categorias_capitan[categoria_izq] < categorias_capitan[categoria_der]:
            categorias_final.append(lista_categoria_izq.pop(0))
        else:
            categorias_final.append(lista_categoria_der.pop(0))
            cantidad_inversiones += len(lista_categoria_izq)
    
    
    if (len(lista_categoria_izq) > 0):
        categorias_final += lista_categoria_izq
        cantidad_inversiones += len(lista_categoria_izq) * len(lista_categoria_der)
    
    if (len(lista_categoria_der) > 0):
        categorias_final += lista_categoria_der
        
    return categorias_final, cantidad_inversiones

def contar_inversiones(lista_categorias, categorias_capitan):
    longitud_categorias = len(lista_categorias)
    
    if longitud_categorias == 1: return lista_categorias, 0
    
    mitad = longitud_categorias // 2
    parte_izquierda = lista_categorias[:mitad]
    parte_derecha = lista_categorias[mitad:]
    
    parte_ordenado_izq, inversiones_izq = contar_inversiones(parte_izquierda, categorias_capitan)
    parte_ordenado_der, inversiones_der = contar_inversiones(parte_derecha, categorias_capitan)
    final_ordenado, cantidad_inversiones = calcular_inversiones(parte_ordenado_izq, parte_ordenado_der, categorias_capitan)
    cantidad_inversiones += inversiones_izq + inversiones_der
    
    return final_ordenado, cantidad_inversiones

def main():
    #lista = [1, 2, 3, 4, 5]
    lista = [1, 9, 6, 4, 5]
    #lista = [8, 1, 7, 2, 6, 3, 5, 4]
    
    diccionario = crear_diccionario_capitan(lista)
    
    a, inv_a = contar_inversiones(lista, diccionario)
    print(f"{a} en {inv_a}")
    
    #lista_b = lista[::-1]
    lista_b = [5, 1, 9, 6, 4]
    print(f"{lista} - {lista_b}")
    b, inv_b = contar_inversiones(lista_b, diccionario)
    print(f"{b} en {inv_b}")
    
    return 0
    
if __name__ == "__main__":
    main()