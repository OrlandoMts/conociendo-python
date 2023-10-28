from random import choice
'''
El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida.
'''

def find_letter(letter, word):
	start_index = 0
	list_index = []
	for i in range(len(word)):
		j = word.find(letter, start_index)
		if j!=-1:
			start_index = j+1
			list_index.append(start_index)

	return list_index

def start_game(lives, word):
	# print(f"palabra generada: {word}")
	hide_word = list("_"*len(word))
	print(f"La palabra es: {hide_word}")
	while lives > 0:
		letter_by_user = input("Ingresa una letra: ").upper()
		
		list_index = find_letter(letter_by_user, word)
		if(len(list_index) == 0):
			lives -= 1
			print(f"[X] Ups! Te quedan {lives} vidas\n")

		for index in list_index:
			hide_word[index - 1] = letter_by_user
			
		print(hide_word)

		if "_" not in hide_word:
			print(f"Felicidades, completaste la palabra y te quedarón {lives} vidas")
			break

	
	if lives == 0:
		return "=== PERDISTE: Se ahorco el monito :/ ==="
	else:
		return f"=== GANASTE: Adivinaste la palabra correcta '{word}'"


def main():
	print("Bienvenido al ahorcado, se generará una palabra aleatoriamente y debes descubrila")
	lives = 7
	words = ["PC", "PERSONA", "ESCRITORIO", "PELICULA", "CONSOLA", "DANIEL"]
	word_random = choice(words)
	return start_game(lives, word_random)

print(main())

