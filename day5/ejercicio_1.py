'''
Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros
.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio
'''

def devolver_distintos(num1, num2, num3):
	list_num = [num1, num2, num3]
	sum_num = sum(list_num)
	print(sum_num)
	if sum_num in range(10, 16):
		list_num.sort()
		return (f"va a devolver el número de valor intermedio {list_num[1]}")
	elif sum_num > 15:
		return (f"va a devolver el número mayor: {max(list_num)}")
	else: 
		return (f"va a devolver el número menor: {min(list_num)}")


print(devolver_distintos(7,2,4))