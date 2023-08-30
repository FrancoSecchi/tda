import sys


def main():
    if len(sys.argv) != 3:
        print("Uso: python contest.py participantes.txt 4")
        return

    archivo_participantes = sys.argv[1]
    pos_capitan = sys.argv[2]


if __name__ == "__main__":
    main()