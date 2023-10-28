import sys
from arturo_utils import leer_caballeros


def maxima_subsecuencia_habilidades(habilidades):
    longitud_habilidades = len(habilidades)
    maximo_calculado = habilidades[0]
    maximo_parcial = maximo_calculado
    index_fin = 0
    i = 1

    while i < longitud_habilidades:
        maximo_parcial = max(maximo_parcial, 0) + habilidades[i]

        if maximo_parcial > maximo_calculado:
            maximo_calculado = maximo_parcial
            index_fin = i

        i += 1

    return maximo_calculado, index_fin


def main():
    if len(sys.argv) != 2:
        print("Uso: python arturo.py caballeros.txt")
        return

    try:
        nombres_caballeros, habilidades = leer_caballeros(sys.argv[1])
    except:
        return

    if len(nombres_caballeros) == 0:
        print("No se han encontrado caballeros")
        return

    maximo_obtenido, idx_fin = maxima_subsecuencia_habilidades(habilidades)

    maximo_parcial = 0
    se_llego_suma = False
    i = idx_fin
    while not se_llego_suma:
        maximo_parcial += habilidades[i]
        se_llego_suma = maximo_parcial == maximo_obtenido
        print(nombres_caballeros[i], end=", " if not se_llego_suma else "")
        i -= 1


if __name__ == "__main__":
    main()
