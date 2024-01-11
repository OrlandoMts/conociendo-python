class Pajaro():
	alas = True

	def __init__(self, color, especie):
		self.color = color
		self.especie = especie

	def piar(self):
		print("Cuak, mi color es {}".format(self.color))

	def volar(self, metros):
		print(f"Estoy volando {metros} metros")

	# Metodo de instancia: puede acceder y modificar atributos de instancia.
	# Puede acceder a otros metodos de instancia.
	# Puede modificar el estado de la clase
	def pintar_negro(self):
		self.color = "Negro"
		print("Ahora mi color es {}".format(self.color))
		self.piar()
		self.alas = True

	# Metodo de clase: no necesitan una instancia para poder ejecutarse.
	# Puede acceder a atributos de clase. (alas)
	# No pueden acceder a atributos de instancia. (color, especie)
	@classmethod
	def poner_huevos(cls, cantidad):
		print("Poniendo huevos {}".format(cantidad))
		print(cls.alas)
		# print(self.color)

	# Metodo estatico: no necesita una instancia para poder ejecutarse.
	# No pueden modificar los atributos de la clase ni de la instancia.
	@staticmethod
	def mirar():
		'''self.color = "Verde"
		cls.alas = False'''
		print("Estoy mirando")


# Ejemplo de instancia: descomentar
'''pato = Pajaro("Blanco", "Pato")
pato.alas = False
print(pato.alas)
pato.pintar_negro()
print(pato.alas)'''

#Ejemplo de classMethod: descomentar
'''Pajaro.poner_huevos(10)
Pajaro.piar()'''

Pajaro.mirar()