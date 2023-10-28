def fibonacci(n):
    a, b = 0, 1
    while(a<n):
        print(a, end=' ')
        a,b = b, b+a


def main():
    cantidad = int(input("Ingresa un cantidad para mostrar la serie fibonnacci: "))
    fibonacci(cantidad)


if __name__ == '__main__':
    main()