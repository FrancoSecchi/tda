def leer_participantes(nombre_archivo, pos_string):
    participantes = []
    capitan = None
    
    pos_capitan = int(pos_string)
    hay_capitan = False
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.split(",", 1)
                nombre_paricipante = datos[0]
                categorias_participante = [ int(x) for x in datos[1].split(",") ]
                
                if (len(participantes) == (pos_capitan - 1)) and not hay_capitan:
                    capitan = {
                        'nombre': nombre_paricipante,
                        'categorias': categorias_participante
                    }
                    hay_capitan = True
                else:
                    participantes.append([nombre_paricipante, categorias_participante])

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
    
    return {
        'participantes': participantes,
        'capitan': capitan
    }
    
def crear_diccionario_capitan(listado_categorias):
    diccionario = {} 
    
    for indice, categoria in enumerate(listado_categorias):
        diccionario[categoria] = indice
        
    return diccionario