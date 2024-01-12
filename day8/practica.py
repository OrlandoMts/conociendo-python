'''Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, 
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).'''


# def generar_sietes():
#     numero = 7
#     while True:
#         yield numero
#         numero += 7


# generador = generar_sietes()
# print(next(generador))
# print(next(generador))
# print(next(generador))


'''Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
1 "Te quedan 3 vidas"
2 "Te quedan 2 vidas"
3 "Te queda 1 vida"
4 "Game Over"
Almacena el generador en la variable perder_vida'''

def perder_vidas():
    vidas = 3
    while vidas > 0:
        yield f"'Te quedan {vidas} vida{'s' if vidas != 1 else '' }'"
        vidas -= 1
    yield "Game Over"
    
perder = perder_vidas()
print(next(perder))
print(next(perder))
print(next(perder))
print(next(perder))