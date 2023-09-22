import sys

mejor_solucion_candidatos = []
mejor_solucion_habilidades = []

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

def obtener_descendientes(nro):
    idx_descendientes = []

    for i in range(len(candidatos_nombres)):
        if i >= nro:
            idx_descendientes.append(i)
    
    return idx_descendientes


def or_binario(lista1, lista2):
    lista_aux = []
    for i in range(len(lista1)):
        lista_aux.append(lista1[i] or lista2[i])
    
    return lista_aux


def backtrack(contrataciones_actuales, habilidades_actuales, nro):
    global mejor_solucion_candidatos
    global mejor_solucion_habilidades
    global max_candidatos

    
    descendientes = obtener_descendientes(nro)
    descendientes_costo = {}

    for idx_descendiente in descendientes:
        habilidades_ampliadas = or_binario(habilidades_actuales.copy(), candidatos_habilidades[idx_descendiente])

        cant_habilidades_cubiertas = sum(habilidades_ampliadas)
        descendientes_costo[idx_descendiente] = cant_habilidades_cubiertas
    
    descendientes_no_explorados = len(descendientes)
    
    while descendientes_no_explorados > 0:
        descendientes_no_explorados -= 1
        idx_mejor_descendiente = max(descendientes_costo, key=lambda k: descendientes_costo[k])
        costo_mejor_descendiente = descendientes_costo[idx_mejor_descendiente]
        contrataciones_proximas = contrataciones_actuales[:] + [candidatos_nombres[idx_mejor_descendiente]]
        habilidades_proximas = or_binario(habilidades_actuales.copy(), candidatos_habilidades[idx_mejor_descendiente])

        del descendientes_costo[idx_mejor_descendiente]

        print(contrataciones_proximas)

        if costo_mejor_descendiente > sum(habilidades_actuales) and len(contrataciones_proximas) < len(mejor_solucion_candidatos):
            if sum(habilidades_proximas) == len(habilidades_proximas):
                mejor_solucion_candidatos = contrataciones_proximas
                mejor_solucion_habilidades = habilidades_proximas
                print("SOLUCION")
                return
        
            backtrack(contrataciones_proximas, habilidades_proximas, nro+1)
    
    return


if len(sys.argv) != 3:
    print("Uso: python antarctic_base.py habilidades.txt candidatos.txt")
    exit

archivo_habilidades = sys.argv[1]
archivo_candidatos = sys.argv[2]

# Leo los dos arhcivos
habilidades = leer_habilidades(archivo_habilidades)
candidatos = leer_candidatos(archivo_candidatos, len(habilidades))
candidatos_nombres = list(candidatos.keys())
candidatos_habilidades = list(candidatos.values())

mejor_solucion_candidatos = candidatos_nombres
mejor_solucion_habilidades = [1] * len(habilidades)

habilidades_cubiertas = [0] * len(habilidades)
nro = 0
contrataciones = []
max_candidatos = len(candidatos)

backtrack(contrataciones, habilidades_cubiertas, nro)

print("\n")
print("Mejor solucion:", mejor_solucion_candidatos)