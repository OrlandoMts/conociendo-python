# phrase = input("Ingresa una frase: ")
phrase = "Este es un texto de prueba, me servira para resolver el proyecto el proyecto de python".lower()
ph_list = list(phrase)
aux_list_phrase = phrase.split(' ')

# 1 Cuantas veces aparece cada letra capturada
print(f"La letra 'y' aparece { ph_list.count('y') } veces repetidas")
# 2 Cuantas palabras hay en total 
print(f"En total hay {len(aux_list_phrase)}")
# 3 Primera y ultima letra
print(f"Primer letra: {ph_list[0]} - Ultima letra {ph_list[-1]}")
# 4 palabras en orden inverso
print(f"En orden inverso: {phrase[::-1]}")
# 5 aparece python?
auxPython = ('python' in aux_list_phrase)
print(f"¿Esta la palabra python en el texto? {auxPython}")  