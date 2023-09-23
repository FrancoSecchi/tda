def calcular_inversiones(lista_categoria_izq, lista_categoria_der, categorias_capitan):
    categorias_final = []
    cantidad_inversiones = 0 
    
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

def obtener_cantidad_inversiones(lista_categorias, categorias_capitan):
    _, cantidad_inversiones = contar_inversiones(lista_categorias, categorias_capitan)
    
    return cantidad_inversiones