import math
def main():
    #escribe tu código abajo de esta línea
    num = int(input("Dame un número: "))

    if num < 0:
        x = "Es negativo"
    elif num > 0:
        x = "Es positivo"
    else:
        x = "Es cero"

    print(x)

    


if __name__ == '__main__':
    main()
