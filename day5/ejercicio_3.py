'''
Escribe una función que requiera una cantidad indefinida de argumentos. 
Lo que hará esta función es devolver True si enalgún momento se ha ingresado al numero cero repetido dosveces consecutivas.

Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''

def duplicate_cero(*args):
	prev = 1
	result = False
	for arg in args:
		if arg == 0 and arg == prev :
			result = True
		prev = arg
	return result

print(duplicate_cero(6,0,5,1,0,3,0,1))