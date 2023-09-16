import sys

mejor_solucion = []
mejor_cant_de_habilidades = 0

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
                habilidades = [ int(x) for x in datos[1].split(",") ]
                candidatos[datos[0]] = [0] * n
                for x in datos[1].split(","):
                    candidatos[datos[0]][int(x) - 1] = 1

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {str(e)}")
    
    return candidatos

def calcular_habilidades_por_cubrir(habilidades_cubiertas):
    return len(habilidades_cubiertas) - sum(habilidades_cubiertas)

def or_binario(lista1, lista2):
    lista_aux = []
    for i in range(len(lista1)):
        lista_aux.append(lista1[i] or lista2[i])
    
    return lista_aux


def backtrack(contrataciones_actuales, habilidades_actuales, nro):
    global mejor_solucion
    global mejor_cant_de_habilidades 

    if nro - 1 >= N:
        return
    
    print("\n")
    print("Nro:", nro)
    print("Mejor solucion:", mejor_solucion)
    print("Mejor cantidad de habilidades:", mejor_cant_de_habilidades)
    print("Contrataciones acutales:", contrataciones_actuales)
    print("Habilidades actuales:", habilidades_actuales)
    # Obtengo los datos del candidato a sumar
    candidato1_nombre = candidatos_nombres[nro-1]
    candidato1_habilidades = candidatos_habilidades[nro-1]

    # Copio el estado actual en nuevas variables
    contrataciones_caso_1 = contrataciones_actuales.copy()
    habilidades_caso_1 = habilidades_actuales.copy()

    # Agrego la nueva contratación
    contrataciones_caso_1.append(candidato1_nombre)

    # Realizo OR entre las habilidades_actuales y las del candidato
    habilidades_caso_1 = or_binario(habilidades_caso_1, candidato1_habilidades)

    # Calculo las estadisticas actuales y caso_1
    cant_habilidades_actuales = sum(habilidades_actuales)
    cant_contrataciones_actuales = len(contrataciones_actuales)

    cant_habilidades_por_cubrir_caso_1 = calcular_habilidades_por_cubrir(habilidades_caso_1)
    cant_habilidades_caso_1 = sum(habilidades_caso_1)
    cant_contrataciones_caso_1 = len(contrataciones_caso_1)

    # Si es el ultimo elemento
    if nro == N:
        if cant_habilidades_actuales <= K and cant_habilidades_actuales > mejor_cant_de_habilidades and cant_contrataciones_actuales < len(mejor_solucion):
            mejor_solucion = contrataciones_actuales.copy()
            mejor_cant_de_habilidades = cant_habilidades_actuales
            return
        
        if cant_habilidades_caso_1 <= K and cant_habilidades_caso_1 > mejor_cant_de_habilidades and cant_contrataciones_caso_1 < len(mejor_solucion):
            mejor_solucion = contrataciones_caso_1.copy()
            mejor_cant_de_habilidades = cant_habilidades_caso_1
            return
   
    # Sino, miro el proximo candidato
    else:
        # Busco al proximo candidato
        candidato2_nombre = candidatos_nombres[nro]
        candidato2_habilidades = candidatos_habilidades[nro]

        contrataciones_caso_2 = contrataciones_actuales.copy()
        habilidades_caso_2 = habilidades_actuales.copy()

        contrataciones_caso_2.append(candidato2_nombre)
        habilidades_caso_2 = or_binario(habilidades_caso_2, candidato2_habilidades)

        cant_habilidades_por_cubrir_caso_2 = calcular_habilidades_por_cubrir(habilidades_caso_2)
        cant_habilidades_caso_1 = sum(habilidades_caso_2)
        cant_contrataciones_caso_1 = len(contrataciones_caso_2)

        if cant_habilidades_por_cubrir_caso_1 == 0:
            if cant_contrataciones_caso_1 < len(mejor_solucion) or mejor_solucion == []:
                mejor_solucion = contrataciones_caso_1
                mejor_cant_de_habilidades = cant_habilidades_caso_1
            return

        if cant_habilidades_por_cubrir_caso_1 <= cant_habilidades_por_cubrir_caso_2:
            backtrack(contrataciones_caso_1, habilidades_caso_1, nro+1)
            backtrack(contrataciones_caso_2, habilidades_caso_2, nro+2)
        else:
            backtrack(contrataciones_caso_2, habilidades_caso_2, nro+2)
            backtrack(contrataciones_caso_1, habilidades_caso_1, nro+1)




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

# Ordeno el diccionario de candidatos segun la cantidad de habilidades
candidatos_ordenados = dict(sorted(candidatos.items(), key=lambda x: sum(x[1]), reverse=True))

habilidades_cubiertas = [0] * len(habilidades)
nro = 1
contrataciones = []
K = len(habilidades_cubiertas)
N = len(candidatos)

backtrack(contrataciones, habilidades_cubiertas, nro)

print("\n")
print("Mejor solucion:", mejor_solucion)