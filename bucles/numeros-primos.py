def primos():
    aux = 0
    for i in range(1,15):
        if i == 1:
            continue
        if i % 1 == 0 and i % i == 0:
            aux += 1
        if aux != 0:
            print(i)
        else:
            pass


if __name__ == '__main__':
    primos()