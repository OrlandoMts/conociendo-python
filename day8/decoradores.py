# Ejemplo
'''def cambiar_letras(tipo):
		def mayusculas(texto):
			print(texto.upper())


		def minusculas(texto):
			print(texto.lower())
			

		if tipo == 'upper':
			return mayusculas
		elif tipo == 'lower':
			return minusculas
		

operacion = cambiar_letras('upper')
operacion('hola')'''


def decorador(funcion):

	def envoltura(palabra):
		print('Esta es la funcion envoltura')
		funcion(palabra)
	
	return envoltura


def mayusculas(texto):
	print(texto.upper())

mayusculas_decorada = decorador(mayusculas)

mayusculas_decorada('hola decorada')
mayusculas('hola')