from random import choice
'''
El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida.
'''

def find_letter(letter, word):
	return [i for i, char in enumerate(word) if char == letter]

def start_game(lives, word):
	# print(f"palabra generada: {word}")
	hide_word = list("_"*len(word))
	print(f"La palabra es: {' '.join(hide_word)}")

	while lives > 0:

		while True:
			letter_by_user = input("Ingresa una letra: ").upper()
			if letter_by_user.isalpha() and len(letter_by_user) == 1:
				break
			else:
				print("Por favor, ingresa una sola letra")
        
		
		list_index = find_letter(letter_by_user, word)
		if not list_index:
			lives -= 1
			print(f"[X] Ups! Te quedan {lives} vida{'s' if lives != 1 else ''}\n")

		for index in list_index:
			hide_word[index] = letter_by_user
			
		print(f"{' '.join(hide_word)}")

		if "_" not in hide_word:
			print(f"Felicidades, completaste la palabra y te quedaron {lives} vida{'s' if lives != 1 else ''}")
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

