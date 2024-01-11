class Animal():

	def __init__(self, edad, color):
		self.edad = edad
		self.color = color

	def nacer(self):
		print("El animal ha nacido")

	def hablar(self):
		print("El animal esta hablando")

class Pajaro(Animal):

	def __init__(self, edad, color, altura_vuelo):
		super().__init__(edad, color)
		self.altura_vuelo = altura_vuelo

	def hablar(self):
		print("pio")
	
	def volar(self, metros):
		print(f"El pajaro ha volado {metros} metros")





piolin = Pajaro(2, "rojo", 100)
piolin.hablar()
piolin.volar(2)