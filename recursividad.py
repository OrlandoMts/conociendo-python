def sum(n):
    total = 0
    for index in range(n+1):
        total += index
        print(total)
    return total

"""
result = sum(3)
print(result)
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print(factorial(num))