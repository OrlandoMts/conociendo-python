class Pajaro():
	alas = True

	def __init__(self, color, especie):
		self.color = color
		self.especie = especie

	def piar(self):
		print("Cuak, mi color es {}".format(self.color))

	def volar(self, metros):
		print(f"Estoy volando {metros} metros")

pato = Pajaro("Blanco", "Pato")
pato.piar()
pato.volar(100)