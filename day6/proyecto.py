from pathlib import Path
import os, shutil
from datetime import datetime
from os import system

def print_categories_folder(base_path):
	print("Categorias disponibles: \n")
	for root, dirs, files in os.walk(base_path):
			for dir in dirs:
				print(dir)

def print_recipes_folder(base_path):
	print("Recetas disponibles: \n")
	for root, dirs, files in os.walk(base_path):
			for fil in files:
				print(fil)

def count_files_in_directory(directory):
	file_count = 0
	if os.path.exists(directory):
		for root, dirs, files in os.walk(directory):
			file_count += len(files)
	return file_count

def read_recipe(base_path):
	system("cls")
	print("\nLectura de receta\n")
	print_categories_folder(base_path)
	name_category = input("Ingrese el nombre de la categoria para mostrar las recetas disponibles: ").lower()
	system("cls") #print("\n")
	folder_category = Path(base_path, name_category)
	if not folder_category.exists():
		return print(f"La categoria {name_category} no existe en el recetario.\n")
	print_recipes_folder(folder_category)
	name_recipe = input("Ingrese el nombre de la receta a leer: ").lower()
	file_recipe = Path(folder_category, f"{name_recipe}.txt")
	if not file_recipe.exists():
		print(f"La receta {name_recipe} no existe en el recetario.\n")
	else:
		with open(file_recipe, 'r') as f:
			print(f.read())

def create_recipe_book(base_path):
	system("cls")
	print("\nCreacion de receta\n")
	print_categories_folder(base_path)
	name_category = input("Ingrese el nombre de la categoria en la cual se guardará la receta: ").lower()
	path_folder = Path(base_path, name_category)
	if not path_folder.exists():
		return print(f"La categoria {name_category} no existe en el recetario.\n")
	name_recipe = input("Ingrese el nombre de la receta a crear: ").lower()
	path_file_recipe = Path(path_folder, f"{name_recipe}.txt")
	if path_file_recipe.exists():
		return print(f"La receta {name_recipe} ya existe en el recetario.\n")
	else:
		path_file_recipe.touch()
		ingredients = input("Ingrese los ingredientes de la receta (separados por coma): ")
		instructions = input("Ingrese las instrucciones de la receta: ")
		path_file_recipe.write_text(f"{ingredients}\n{instructions}\nFecha de creacion: {datetime.now():%Y-%m-%d %H:%M:%S}\nCantidad de archivos: {count_files_in_directory(path_folder)}\n")

def delete_recipe(base_path):
	system("cls")
	print("\nEliminación de receta\n")
	print_categories_folder(base_path)
	name_category = input("Ingrese el nombre de la categoria para mostrar las recetas disponibles: ").lower()
	system("cls")
	folder_category = Path(base_path, name_category)
	if not folder_category.exists():
		return print(f"La categoria {name_category} no existe en el recetario.\n")
	print_recipes_folder(folder_category)
	name_recipe = input("Ingrese el nombre de la receta a eliminar: ").lower()
	file_recipe = Path(folder_category, f"{name_recipe}.txt")
	if not file_recipe.exists():
		print(f"La receta {name_recipe} no existe en el recetario.\n")
	else:
		os.remove(file_recipe)
		print(f"La receta {name_recipe} ha sido eliminada del recetario\n")

def create_category(base_path):
	system("cls")
	print("\nCreacion de categoria\n")
	name_category = input("Ingrese el nombre de la categoria a crear: ").lower()
	folder_category = Path(base_path, name_category)
	if not folder_category.exists():
		folder_category.mkdir()
		print(f"La categoria {name_category} ha sido creada\n")
	else:
		print("La categoria ya existe, prueba con otro nombre\n")

def delete_category(base_path):
	system("cls")
	print("\nEliminación de categoria\n")
	print("Si una categoria contiene archivos tambien los eliminará\n")
	print_categories_folder(base_path)
	name_category = input("Ingrese el nombre de la categoria a eliminar: ").lower()
	folder_category = Path(base_path, name_category)
	if not folder_category.exists():
		print(f"La categoria {name_category} no existe en el recetario.\n")
	else:
		try:
			folder_category.rmdir()
			print(f"La categoria {name_category} ha sido eliminada del recetario\n")
		except OSError:
			shutil.rmtree(folder_category)
			print(f"La categoria {name_category} y sus archivos han sido eliminados del recetario\n")


def print_cli(base_path):
	option = 0
	while option != 6 :
		print("1. Leer receta\n2. Crear receta\n3. Crear categoria\n4. Eliminar receta\n5. Eliminar categoria\n6. Finalizar programa\n")
		try:
			option = int(input("Elige una opcion ") )
			match option:	
				case 1:
					read_recipe(base_path)
				case 2:
					create_recipe_book(base_path)
				case 3:
					create_category(base_path)
				case 4:
					delete_recipe(base_path)
				case 5:
					delete_category(base_path)
				case 6:
					print("Hasta luego")
				case _:
					print("Opcion no valida")
		except ValueError:
			print("Por favor, ingresa un número válido.")

		

def main():
	print("Bienvenido al recetario de Orlando Montes\n")
	base_path = Path.home()
	base_recipe_book = Path(base_path, 'Recetas')
	print(f"Existen: {count_files_in_directory(base_recipe_book)} recetas en total\n")
	print_cli(base_recipe_book)
	

if __name__ == "__main__":
    main()