from functools import reduce


my_list = [1,2,3,4,5]

toReduce = reduce(lambda i,j: i+j, my_list)

print(toReduce)