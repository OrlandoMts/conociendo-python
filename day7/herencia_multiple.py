class Padre:
	def hablar(self):
		print("Soy tu padre")

class Madre:
	def hablar(self):
		print("Soy tu madre")

	def reir(self):
		print("jajaja")

class Hijo(Madre, Padre):
	pass

class Hijo2(Padre, Madre):
	pass

class Nieto(Hijo):
	pass



mi_hijo = Hijo()
mi_hijo.hablar()

mi_hijo2 = Hijo2()
mi_hijo2.hablar()

mi_nieto = Nieto()
mi_nieto.hablar()
