class CD:
	def __init__(self, autor, titulo, canciones) -> None:
		self.autor = autor 
		self.titulo = titulo 
		self.canciones = canciones

	def __str__(self) -> str:
		return f"CD: {self.titulo} - {self.autor} - {self.canciones} canciones"
	
	def __len__(self) -> int:
		return self.canciones
	
	def __del__(self) -> None:
		print("Se ha eliminado la instancia de la clase CD")

mi_cd = CD("Pink Floyd", "the wall", 24)

print(str(mi_cd))
print(len(mi_cd))

# Elimina la instancia creada de la clase CD
del mi_cd 
print(len(mi_cd))
