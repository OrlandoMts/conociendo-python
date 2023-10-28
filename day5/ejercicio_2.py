'''
Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, 
y quedevuelva todas sus letras únicas (sin repetir) pero en ordenalfabético.

Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
'''

def transform_text(text):
	# list_text = sorted(list(text))
	list_text = list(set(text))
	return sorted(list_text)

print(transform_text("entretenido"))