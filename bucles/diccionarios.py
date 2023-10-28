def main():
    libros_biblia = {
        'genesis': 50,
        'exodo': 40,
        'levitico': 27,
        'numeros': 36,
        'deuteronomio': 34,
    }

    # libros_biblia.keys()
    # libros_biblia.values()
    # libros_biblia.items()
    for libro, capitulos in libros_biblia.items():
        print("El libro del pentateuco " + libro + " tiene " + str(capitulos) + " capitulos.")


if __name__ == '__main__':
    main()