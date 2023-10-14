import sys

mejor_solucion_candidatos = None
mejor_solucion_habilidades = None

def leer_habilidades(nombre_archivo):
    habilidades = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                habilidades.append(linea.split(",")[1].strip())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
    
    return habilidades

def leer_candidatos(nombre_archivo, n):
    candidatos = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.split(",", 1)
                candidatos[datos[0]] = [0] * n
                for x in datos[1].split(","):
                    candidatos[datos[0]][int(x) - 1] = 1

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
    
    return candidatos

def obtener_descendientes(contrataciones_actuales):
    return [x for x in candidatos_nombres if x not in set(contrataciones_actuales)]

def or_binario(lista1, lista2):
    lista_aux = []
    for i in range(len(lista1)):
        lista_aux.append(lista1[i] or lista2[i])
    
    return lista_aux

def backtrack(contrataciones_actuales, habilidades_actuales):
    global mejor_solucion_candidatos
    global mejor_solucion_habilidades
    global max_candidatos

    descendientes = obtener_descendientes(contrataciones_actuales)
    descendientes_costo = {}

    for nombre_descendiente in descendientes:
        habilidades_ampliadas = or_binario(habilidades_actuales, candidatos[nombre_descendiente])

        cant_habilidades_cubiertas = sum(habilidades_ampliadas)
        descendientes_costo[nombre_descendiente] = cant_habilidades_cubiertas
    
    descendientes_no_explorados = len(descendientes)
    
    while descendientes_no_explorados > 0:
        descendientes_no_explorados -= 1

        nombre_mejor_descendiente = max(descendientes_costo, key=lambda key: descendientes_costo[key])
        costo_mejor_descendiente = descendientes_costo[nombre_mejor_descendiente]
        contrataciones_proximas = contrataciones_actuales[:] + [nombre_mejor_descendiente]
        habilidades_proximas = or_binario(habilidades_actuales, candidatos[nombre_mejor_descendiente])

        del descendientes_costo[nombre_mejor_descendiente]

        if costo_mejor_descendiente > sum(habilidades_actuales):
            if mejor_solucion_candidatos is None or (len(contrataciones_proximas) < len(mejor_solucion_candidatos)):
                if sum(habilidades_proximas) == len(habilidades_proximas):
                    mejor_solucion_candidatos = contrataciones_proximas
                    mejor_solucion_habilidades = habilidades_proximas
                    return

                backtrack(contrataciones_proximas, habilidades_proximas)
    
    return

def imprimir_nombres_solucion():
    [print(nombre) for nombre in mejor_solucion_candidatos]

if len(sys.argv) != 3:
    print("Uso: python antarctic_base.py habilidades.txt candidatos.txt")
    exit()

archivo_habilidades = sys.argv[1]
archivo_candidatos = sys.argv[2]

# Leo los dos arhcivos
habilidades = leer_habilidades(archivo_habilidades)
candidatos = leer_candidatos(archivo_candidatos, len(habilidades))
candidatos_nombres = list(candidatos.keys())

max_candidatos = len(candidatos)

contrataciones_inicial = []
hab_cubiertas_inicial = [0] * len(habilidades)

backtrack(contrataciones_inicial, hab_cubiertas_inicial)

if mejor_solucion_candidatos is None:
    print("Los candidatos posibles no cubren todas las habilidades requeridas")
else:
    imprimir_nombres_solucion()
