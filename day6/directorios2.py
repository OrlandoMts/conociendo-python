from pathlib import Path

carpeta = Path('/Users/omontes/desarrollos/nuevo-portal/01desarrollos/python/bases/day6')
archivo = carpeta / 'archivo_dir.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()