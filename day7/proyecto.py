from os import system

class Persona:
	def __init__(self, nombre, apellidos) -> None:
		self.nombre = nombre
		self.apellidos = apellidos

class Cliente(Persona):
	def __init__(self, nombre, apellidos, numero_cuenta, balance) -> None:
		super().__init__(nombre, apellidos)
		self.numero_cuenta = numero_cuenta
		self.balance = balance # Saldo que tiene la cuenta

	def __str__(self) -> str:
		return f'Nombre: {self.nombre}\nApellidos: {self.apellidos}\nNumero de cuenta: {self.numero_cuenta}\nBalance actual (saldo disponible): ${self.balance}'
	
	def __del__(self) -> None:
		print(">>> Se ha eliminado la instancia de la clase Cliente")
	
	def depositar(self, deposito):
		try:
			if deposito < 0:
				raise ValueError('No se puede depositar un valor negativo')
			self.balance += deposito
		except ValueError as e:
			print(f"Error: {e}")
		else:
			return f">>> Saldo actual: ${self.balance} "	
	
	def retirar(self, retiro):
		try:
			if self.balance == 0:
				raise ValueError('No se puede retirar si no hay saldo disponible')
			if retiro < 0:
				raise ValueError('No se puede retirar un valor negativo')
			if retiro > self.balance:
				raise ValueError('No se puede retirar un valor mayor al saldo disponible')
			self.balance -= retiro
			return f">>> Saldo actual: ${self.balance}"
		except ValueError as e:
			print(f"Error: {e}")

# TODO: crear logica para realizar transacciones (depositar, retirar, salir)

def menu_cli(obj: Cliente) -> None:
	option = 0
	while option != 3 :
		print("1. Depositar - 2. Retirar - 3. Salir")
		try:
			option = int(input("Elige una opcion ") )
			match option:
				case 1:
					try:
						print(obj.depositar(int(input("Ingrese el monto a depositar: "))))
						print("\n")
					except ValueError as e:
						print(f"Error: {e}")
				case 2:
					try:
						print(obj.retirar(int(input("Ingrese el monto a retirar: "))))
						print("\n")
					except ValueError as e:
						print(f"Error: {e}")
				case 3:
					print("Adios!")
					del obj
				case _:
					print("Opción no valida")
		except ValueError:
			print("Por favor, ingrese una opción valida.")
	
def crear_cliente() -> Cliente:
	try:
		nombre = input("Ingrese su nombre: ")
		apellidos = input("Ingrese sus apellidos: ")
		numero_cuenta = int(input("Ingrese su numero de cuenta: "))
		balance = int(input("Ingrese su saldo: "))
		system("cls")
		return Cliente(nombre, apellidos, numero_cuenta, balance)
	except ValueError:
		print("Ha ingresado un dato incorrecto, intentelo de nuevo")
	
def main():
	print("==========Bienvenido al banco==========")
	# mi_cliente = crear_cliente()
	mi_cliente = Cliente("Orlando", "Montes", 1234, 1000)
	print(str(mi_cliente))
	print("\n\n")
	menu_cli(mi_cliente)

if __name__ == "__main__":
	main()