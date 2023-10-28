def pascal():
    filas = []
    numero = 3
    expansion = ""
    value = numero

    for i in range(numero):
        lon_filas = len(filas)
        print(f"longitud {lon_filas}")
        fila_nueva = [1]
        print(f"fila nueva: {fila_nueva}")
        
        for j in range(lon_filas-1):
            print(f'El valor de j {j}')
            calculo = filas[j] + filas[j+1]
            print(f"El valor de filas[j]: {filas[j]}")
            print(f"El valor de filas[j+1]: {filas[j+1]}")
            print(f"El valor de calculo: {calculo}")

            fila_nueva.append(calculo)
        
        fila_nueva.append(1)
        # expansion = "\t".expandtabs(value)
        value -= 1
        print("{}{}".format(expansion,fila_nueva))
        filas = fila_nueva


if __name__ == '__main__':
    pascal()