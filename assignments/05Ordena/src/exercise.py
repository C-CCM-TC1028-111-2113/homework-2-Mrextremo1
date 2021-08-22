def main():
    # Escribe el código adecuado para completar el programa
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))
    x = int()
    y = int()
    z = int()

    if num1 < num2:
        if num3 < num2:
            if num1 < num3:
                x = num2
                y = num3
                z = num1
            elif num1 > num3:
                x = num2
                y = num1
                z = num3
        
            
    if num3 > num1:
        if num3 > num2:
            if num2 > num1:
                x = num3
                y = num2
                z = num1
            elif num1 > num2:
                x = num3
                y = num1
                z = num2
    elif num3 < num2:
        x = num1
        y = num2 
        z = num3
    else:
        x = num1
        y = num3
        z = num2
    
    print(z)
    print(y)
    print(x)


if __name__=='__main__':
    main()
