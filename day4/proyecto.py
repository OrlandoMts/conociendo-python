from random import randint

player = input("Ingresa tu nombre: ")
print(f"Bueno, {player}, he pensado un número entre 1 y 100\ntienes solo ocho intentos para adivinar cuál crees que es el número")
random_number = randint(1,100)
attempts = 8
aux_attempts = 8
while(attempts > 0):
	try:
			attempts -= 1
			input_number = int(float(input("Ingresa el numero: ")))
			print("Número ingresado:", input_number)
			
			if input_number not in range(1,101):
				print("El numero ingresado esta fuera de rango, intentalo de nuevo")
			elif input_number < random_number:
				print("El numero ingresado es menor, intentalo de nuevo")
			elif input_number > random_number:
				print("El numero ingresado es mayor, intentalo de nuevo")
			else: 	
				print(f"Acertaste!! Te tomó {aux_attempts - attempts} intentos lograrlo :)")
				break

	except ValueError:
			print("Error: Por favor, ingresa un número entero.")