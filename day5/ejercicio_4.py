'''
Escribe una función llamada contar_primos() que requiera un solo argumento numérico.

Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va desde cero hasta ese número incluido, 
y va a devolver la cantidad de números primos que encontró.

Aclaración, por convención el 0 y el 1 no se consideran primos.
'''

def contar_primos(limit):
	gen_range = list(range(limit + 1))
	result = []
	for item in gen_range:
		if item == 0 or item == 1:
			continue
		if item % 1 == 0 and item % item == 0:
			result.append(item)
	
	print(f"primos: {result}")
	return gen_range

print(contar_primos(100))