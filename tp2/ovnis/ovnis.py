import sys
from grafo import Grafo
from grafo_utils import ExeptionGrafo


def main():
    if len(sys.argv) != 2:
        print("Uso: python ovnis.py red.txt")
        return

    try:
        g = Grafo.desde_archivo(sys.argv[1])
    except ExeptionGrafo as e:
        print(e.mensaje)
        return

    flujo_maximo = g.fordFulkerson()

    print(f"La mayor cantidad posible de datos por segundo es: {flujo_maximo}")

    configuracion_red = g.obtener_configuracion_red()
    print('\nConfiguración de la Red (Flujo Real/Capacidad):')
    for u, v, flujo, capacidad in configuracion_red:
        print(f'{u} -> {v}: {flujo}/{capacidad}')

    cuellos_botella = g.obtener_cuellos_de_botella()
    print('\nCuellos de Botella:')
    for u, v in cuellos_botella:
        print(f'{u} -> {v}')

    return 0


if __name__ == "__main__":
    main()
