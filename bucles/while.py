def main():
    i = 1
    resultado = 0
    while resultado < 10:
        base = 2
        resultado = base**i
        i+=1
        print("El resultado de 2 elevado a " + str(i) + " es " + str(resultado))


if __name__ == '__main__':
    main()