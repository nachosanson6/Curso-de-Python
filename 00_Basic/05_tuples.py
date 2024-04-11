
#Las tuples son inmutables

my_tuple = tuple()
my_other_tuple = (50, 90, 25, 84)

my_tuple = (33, 1.78, 'Nacho', 'Sanson')
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])

#Funciones
print(my_tuple.count(33)) #Funciona como en las listas
print(my_tuple.index('Sanson')) #No dice le indice del elemento seleccionado,si hay varios iguales te dice el primer indice. 


# my_tuple[1] = 1.90  #En las tuplas no se puede variar los datos.
# print(my_tuple)

# my_tuple[4] = 'hola' # En las tuplas no se pueden añadir nuevos elementos
# print (my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) #(33, 1.78, 'Nacho', 'Sanson', 50, 90, 25, 84)
print(my_sum_tuple[3:6]) #('Sanson', 50, 90)

# Se puede cambiar entre lista y tupla con list() y tuple()

del my_tuple #No vacía la tupla sino que elimina la tupla entera
print(my_tuple)

