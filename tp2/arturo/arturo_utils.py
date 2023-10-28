def leer_caballeros(nombre_archivo):
    nombres_caballeros = []
    habilidades_caballeros = []

    min_habilidad = None
    index_min_habilidad = 0

    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.split(",", 1)
                nombre_caballero = datos[0]
                habilidad_caballero = int(datos[1])

                nombres_caballeros.append(nombre_caballero)
                habilidades_caballeros.append(habilidad_caballero)

                if (min_habilidad is None) or (habilidad_caballero < min_habilidad):
                    min_habilidad = habilidad_caballero
                    index_min_habilidad = len(habilidades_caballeros) - 1

    except FileNotFoundError as e:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        raise e
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
        raise e

    if index_min_habilidad > 0:
        nombres_caballeros = nombres_caballeros[index_min_habilidad:] + nombres_caballeros[:index_min_habilidad]
        habilidades_caballeros = habilidades_caballeros[index_min_habilidad:] + habilidades_caballeros[:index_min_habilidad]

    return nombres_caballeros, habilidades_caballeros