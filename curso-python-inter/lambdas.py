palindromo = lambda string: string == string[::-1]
sumar = lambda a,b: a + b

""" Es lo mismo que: 
    def palindromo(string):
        return string == string[::-1]
"""

print(palindromo('ana'))
print(sumar(2,4))