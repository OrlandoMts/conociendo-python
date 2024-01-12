def suma():
  a = int(input("Ingrese un numero: "))
  b = int(input("Ingrese un numero: "))
	print(a+b)
	print("Gracias por sumar " + str(a))
	print("Gracias por sumar " + a)

try:
	suma()
except TypeError:
	print("Estas intentando concatener tipos distintos")
except ValueError:
	print("Estas intentando sumar un valor no numerico")
else:
	print("La suma se ejecuto correctamente")
finally:
	print("Se termino el programa")
