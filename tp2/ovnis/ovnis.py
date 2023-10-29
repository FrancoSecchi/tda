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

    print(g)

    return 0


if __name__ == "__main__":
    main()
