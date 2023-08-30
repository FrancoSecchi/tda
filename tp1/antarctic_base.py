import sys
def main():
    if len(sys.argv) != 3:
        print("Uso: python antarctic_base.py habilidades.txt candidatos.txt")
        return

    archivo_habilidades = sys.argv[1]
    archivo_candidatos = sys.argv[2]

if __name__ == "__main__":
    main()