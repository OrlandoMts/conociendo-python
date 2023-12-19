import os

# ruta = os.makedirs("day5/nuevo")
os.rmdir("day5/nuevo")
# os.rmdir('C:\\Users\\omontes\\desarrollos\\nuevo-portal\\01desarrollos\\python\\bases\\day5\\nuevo')

ruta_acceso = 'C:\\Users\\omontes\\desarrollos\\nuevo-portal\\01desarrollos\\python\\bases\\day6'

elemento = os.path.basename(ruta_acceso)
elemento2 = os.path.split(ruta_acceso)

print(elemento)
print(elemento2)
