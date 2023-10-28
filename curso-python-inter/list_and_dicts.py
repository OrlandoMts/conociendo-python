def main():
    my_lits = [1,"hello",4,False,5.6]
    my_dict = {
	"firstName": "Orlando",
	"lastName": "Montes"
    }

    hola = [
        {
            "firstName": "Orlando",
	        "lastName": "Montes"
        },
        {
            "firstName": "Daniel",
	        "lastName": "Antonio"
        }
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    for key, value in super_dict.items():
        print(key, " > ", value)


if __name__ == '__main__':
    main()
