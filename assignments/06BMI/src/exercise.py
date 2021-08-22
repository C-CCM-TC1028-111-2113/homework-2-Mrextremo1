def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    indice = peso/(altura**2)

    if peso <= 0 or altura <= 0:
        x = "Revisa tus datos, alguno de ellos es erróneo"
    elif indice < 20 and indice > 1:
        x = "PESO BAJO"
    elif indice >= 20 and indice < 25:
        x = "NORMAL"
    elif indice >= 25 and indice < 30:
        x = "SOBREPESO"
    elif indice >= 30 and indice < 40:
        x = "OBESIDAD"
    else:
        x = "OBESIDAD MORBIDA"

    print(x)


if __name__=='__main__':
    main()