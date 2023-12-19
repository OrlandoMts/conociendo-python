import os

# Obtiene la ruta completa al archivo
file_path = os.path.join(os.path.dirname(__file__), 'prueba1.txt')
# my_file = open(file_path, 'w')
my_file = open(file_path, 'a')

# my_file.write('Hola mundo\n')
# my_file.write('Segundo parrrafo')
# my_file.writelines(['hey\n', 'Tercer parrafo', 'adios!!\n'])

# Ejemplo para el modo: a
my_file.write('Bienvenido\n')

my_file.close()