def leer_caballeros(nombre_archivo):
    nombres_caballeros = []
    popularidades_caballeros = []

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.split(",", 1)
                nombre_caballero = datos[0]
                popularidad_caballero = int(datos[1])

                nombres_caballeros.append(nombre_caballero)
                popularidades_caballeros.append(popularidad_caballero)

    except FileNotFoundError as e:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        raise e
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
        raise e

    return nombres_caballeros, popularidades_caballeros
