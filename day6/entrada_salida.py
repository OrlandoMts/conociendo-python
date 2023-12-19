import os

# Obtiene la ruta completa al archivo
file_path = os.path.join(os.path.dirname(__file__), 'prueba.txt')
mi_archivo = open(file_path)

# Ejemplo de lectura de un archivo
# print(mi_archivo.read())
# Fin Ejemplo de lectura de un archivo

# Ejemplo de lectura de un archivo línea por línea
# single_line = mi_archivo.readline()
# print(single_line)

# single_line = mi_archivo.readline()
# print(single_line.rstrip())

# single_line = mi_archivo.readline()
# print(single_line)

# Fin Ejemplo de lectura de un archivo línea por línea

# Ejemplo de lectura de un archivo con ciclo
# for line in mi_archivo:
# 	print(f"Aqui dice {line}")
# Fin Ejemplo de lectura de un archivo con ciclo

all_lines = mi_archivo.readlines()
print(all_lines)

# my_file = open(file_path, encoding='US-ASCII', errors='surrogateescape')
# print(my_file.read())

mi_archivo.close()