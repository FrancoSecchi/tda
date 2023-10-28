def leer_caballeros(nombre_archivo):
    nombres_caballeros = []
    popularidades_caballeros = []

    min_popularidad = None
    index_min_popularidad = 0

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.split(",", 1)
                nombre_caballero = datos[0]
                popularidad_caballero = int(datos[1])

                nombres_caballeros.append(nombre_caballero)
                popularidades_caballeros.append(popularidad_caballero)

                if (min_popularidad is None) or (
                    popularidad_caballero < min_popularidad
                ):
                    min_popularidad = popularidad_caballero
                    index_min_popularidad = len(popularidades_caballeros) - 1

    except FileNotFoundError as e:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        raise e
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
        raise e

    if index_min_popularidad > 0:
        nombres_caballeros = (
            nombres_caballeros[index_min_popularidad:]
            + nombres_caballeros[:index_min_popularidad]
        )
        popularidades_caballeros = (
            popularidades_caballeros[index_min_popularidad:]
            + popularidades_caballeros[:index_min_popularidad]
        )

    return nombres_caballeros, popularidades_caballeros
