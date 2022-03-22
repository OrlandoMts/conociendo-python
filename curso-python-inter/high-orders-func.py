def funcStart(func):
    func()


def funcList():
    my_list=[1,2,3,4,5]
    print(my_list)
    return my_list


def funcList2():
    my_list=[6,7,8,9,10]
    print(my_list)
    return my_list


def main():
    funcStart(funcList)
    funcStart(funcList2)


if __name__ == '__main__':
    main()