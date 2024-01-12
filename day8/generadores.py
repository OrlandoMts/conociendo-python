def mi_funcion():
	lista = []
	for i in range(10):
		lista.append(i * 2)
	
	return lista

def mi_generador():
	for i in range(10):
		yield i * 2


print(mi_funcion())
print(mi_generador())

mi_gen = mi_generador()
print(next(mi_gen))
print(next(mi_gen))

def generador_fibbonaci(n):
	a, b = 0, 1
	for i in range(n):
		yield a
		a, b = b, a + b


fibo = generador_fibbonaci(10)
print("Fibbonacci")
try:
	print(next(fibo))
	print(next(fibo))
	print(next(fibo))
	print(next(fibo))
	print(next(fibo))
	'''print(next(fibo))
	print(next(fibo))
	print(next(fibo))
	print(next(fibo))
	print(next(fibo))
	print(next(fibo))'''
except StopIteration:
	print("Fin de la secuencia")



