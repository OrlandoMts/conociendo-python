class BirdTest():
	pass

class Bird():
	instance = None

	@staticmethod
	def get_instance():
		if not Bird.instance:
			# Bird.instance = Bird()
			Bird()
		return Bird.instance
	
	def __init__(self, color, especie):
		if not Bird.instance:
			Bird.instance = self
		self.color = color
		self.especie = especie

# my_bird = BirdTest()
# another_bird = BirdTest()

my_bird = Bird("red", "tucan")
another_bird = Bird("black", "cotorro").get_instance()

print(f"El primer pajaro es de color {my_bird.color} y es un {my_bird.especie}")
print(f"El primer pajaro es de color {another_bird.color} y es un {another_bird.especie}")


print(f"Espacio en memoria - > {my_bird}")
print(f"Espacio en memoria - > {another_bird}")
print(my_bird.color)