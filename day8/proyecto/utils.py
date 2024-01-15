from os import system


def turno_ventanilla():
		for n in range(1, 100000):
			yield f"V-{n}"


def turno_ejecutivo():
		for n in range(1, 100000):
				yield f"E-{n}"


gen_ventanilla = turno_ventanilla()
gen_ejecutivo = turno_ejecutivo()


def decorador(rubro):
	
		system("cls")
		print("\n" + "*" * 23)
		print("Su numero es:")

		if rubro == "V":
			print(next(gen_ventanilla))
		else:
			print(next(gen_ejecutivo))
		print("Pronto le atenderemos.")
		print("*" * 23 + "\n")
	