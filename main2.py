"""
Primeros pasos en python,
A ver como me va...
"""
let_entrada = input("ingresa el número 5: ")

# CONDICIONALES-------*
"""
if(int(entrada)==5):
   print(f"Bien escribiste {entrada}")
else:
    print(f"Error, escribiste {entrada} y no 5") 
"""

# FUNCIONES-------*
def verificarEntrada(entrada):
    if(int(entrada)==5):
        print(f"Bien escribiste {entrada}")
    else:
        print(f"Error, escribiste {entrada} y no 5") 

verificarEntrada(let_entrada)

def registroEdad():
    let_edad = input("Ingresa tu edad: ")
    return let_edad

print(f"Ingresaste que tienes {registroEdad()} años")

# LISTAS---------*
nombres = ["Orlando", "Daniel", "..."]

for nombre in nombres:
    print(nombre)