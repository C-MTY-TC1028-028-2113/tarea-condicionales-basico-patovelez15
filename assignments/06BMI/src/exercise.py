def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    if peso > 0 and altura > 0:
        indice = peso / altura**2
        if indice < 20:
            print("PESO BAJO")
        if indice >= 20 and indice < 25:
            print("NORMAL")
        if indice >= 25 and indice < 30:
            print("SOBREPESO")
        if indice >= 30 and indice < 40:
            print("OBESIDAD")
        if indice >= 40:
            print("OBESIDAD MORBIDA")
    else:
        print("Revisa tus datos, alguno de ellos es erróneo.")

if __name__=='__main__':
    main()