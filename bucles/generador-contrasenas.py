import random


def generarContrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '#', '$', '/', '-']

    caracteres = mayusculas + minusculas + numeros + simbolos
    contrasena = []

    for i in range(13):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    return contrasena


def main():
    contrasena = generarContrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':
    main()