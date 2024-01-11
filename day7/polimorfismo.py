class Vaca:
	def __init__(self, nombre) -> None:
		self.nombre = nombre

	def hablar(self) -> None:
		print(f"{self.nombre} Muuuuuu")

class Oveja:
	def __init__(self, nombre) -> None:
		self.nombre = nombre

	def hablar(self) -> None:
		print(f"{self.nombre} Beeeee")

vaca1 = Vaca("Maria")
oveja1 = Oveja("Lola")
vaca1.hablar()
oveja1.hablar()
