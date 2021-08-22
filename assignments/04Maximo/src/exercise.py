def main():
    #escribe tu código abajo de esta línea
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if num1 < num2:
        if num3 < num2:
            x = num2
        elif num3 > num1:
            x = num3
    elif num3 > num1:
        x = num3
    else:
        x = num1
    
    print(x)


if __name__=='__main__':
    main()
