def pascal():
    input_rows = int(input("Ingresa la cantidad de niveles del triangulo de pascal: "))
    level = []

    for n in range(input_rows):
        level.append([])
        level[n].append(1)
        #print(level)
        for m in range(1, n):
            level[n].append(level[n-1][m-1] + level[n-1][m])

        if(input_rows != 0):
            level[n].append(1)
  
        print(level)

    for n in range(input_rows):
        print(" " * (input_rows - n), end= " ", sep=" ")
        
        for m in range(0, n + 1):
            print('{0:5}'.format(level[n][m]), end=" ", sep=" ")
        
        print()
        


if __name__ == '__main__':
    pascal()