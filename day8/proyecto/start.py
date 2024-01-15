import utils


def menu_cli():
		print("=== Bienvenido al banco de Python===")
		print("\n")

		while True:
				print(">> ¿A donde te quieres dirigir? [V] Ventanilla [E] Ejecutivo ")
				try:
						option = input(">> ").upper()
						["V", "E"].index(option)
				except ValueError:
						print("Esa no es una opción válida")
				else:
						break
				
		utils.decorador(option)


def main():
		while True:
				menu_cli()
				try:
						otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
						["S", "N"].index(otro_turno)
				except ValueError:
						print("Esa no es una opción válida")
				else:
						if otro_turno == "N":
								print("Gracias por su visita")
								break
						else:
								continue
	


if __name__ == "__main__":
	main()