def toSquare(numero):
    try:
        if numero < 0:
            raise ValueError("El numero debe ser mayor de cero")
        print(numero**2)
    except ValueError as ve:
        print(ve)
        return False


def main():
    numero = input("Ingresa un numero para saber su cuadrado: ")
    toSquare(int(numero))    


if __name__ == '__main__':
    main()