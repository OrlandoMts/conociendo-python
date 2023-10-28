from nis import match


print("Bienvenid@ al conversor magico de pesos mx!!")
print("Elige una opcion: ")
print("1. Dolares")
print("2. Wones")

def turnInMoney():
    option = int(input("¿Qué deseas convertir? "))
    match option:
        case 1:
            print("----->ELEGISTE DOLARES")
            print(mxToDollars())
        case 2:
            print("----->ELEGISTE WONES")
            print(mxToWones())
        case _:
            print("Opcion no valida")    


def mxToDollars():
    count = int(input("Cuantos pesos mx quieres convertir a dolares? "))
    dollar = round(count / 20.68, 2)
    return dollar

def mxToWones():
    count = int(input("Cuantos pesos mx quieres convertir a wones? "))
    wone = round(count / 0.017, 2)
    return wone

turnInMoney()