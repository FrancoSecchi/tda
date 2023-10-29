import sys
from grafo import Grafo

def main():
    if len(sys.argv) != 2:
        print("Uso: python ovnis.py red.txt")
        return

    try:
        g = Grafo.desde_archivo(sys.argv[1])
    except:
        return

    print(g)

    return 0


if __name__ == "__main__":
    main()