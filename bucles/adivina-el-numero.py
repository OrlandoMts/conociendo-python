import random


def adivinaElNumero(numeroAleatorio):
    opcion = 0
    while opcion != numeroAleatorio:
        opcion = int(input("Ingresa el número: "))
        if opcion == numeroAleatorio:
            print("¡ACERTASTE! El número generado es: " + str(numeroAleatorio))
        elif opcion < numeroAleatorio:
            print("El número generado es mas grande")
        else:
            print("El número generado es menor")
    

def main():
    print("La computadora generará un número al azar.")
    print("ADIVINALO")
    numeroAleatorio = random.randint(1,10)
    adivinaElNumero(numeroAleatorio)


if __name__ == '__main__':
    main()