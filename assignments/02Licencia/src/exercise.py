
def main():
    #Escribe tu código debajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    id = str(input("¿Tienes identificación oficial? (s/n): "))

    if edad >= 18:
        if id == str("s"):
            x = "Trámite de licencia concedido"
        elif id == str("n"):
            x = "No cumples requisitos"
        else:
            x = "Respuesta incorrecta"
    elif edad < 18 and edad > 0:
        x = "No cumples requisitos"
    else:
        x = "Respuesta incorrecta"
    
    print(x)


if __name__ == '__main__':
    main()
