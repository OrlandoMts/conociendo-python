my_list = [1,2,3,4,5]
my_list2 = list([6,7,8,9])

#Para agregar elementos al final
my_list.append('ultimo elemento insertado')
#Para agregar dependiendo la posicion (index,elemento)
my_list.insert(2, 2.5)

#Elemina el primer elemento encontrado que coincida con dicho elemento
my_list2.remove(7)

for ele in my_list:
    print(ele)

for value in my_list2:
    print(value)

#con el metodo .pop() elimina un elemento dado un index, sino se le pasa nada
#por default elimina el ultimo

#Para ordernar una lista en forma ascendente se usa .sort()
#Para limpiarla se usa .clear()
