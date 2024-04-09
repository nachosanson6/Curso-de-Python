
my_list = list()
my_other_list = [33, 1.78, 'Nacho', 'Sansón']

print(len(my_list))

my_list = [35, 24, 60, 30, 56, 25, 78]
print(my_list)
print(len(my_list))
print(type(my_list))

print(my_list[0])
print(my_list[-1])
print(my_list[-3])
print(my_list.count(24))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

#Funciones
my_other_list.append('mouredev') #Inserta un nuevo dato al final
print(my_other_list)

my_other_list.insert(1,'rojo') # Inserta un dato en la posición que le indiquemos
print(my_other_list)

my_other_list[1] = 'azul'
print(my_other_list)

my_other_list.remove('azul') # Elimina el dato que le indiquemos. Si hay varios elementes con el mosmo nombre o dato, elimina solo el primero
print(my_other_list)

my_list.pop() #Elimina el último dato de la lista. Si pongo un indice entre los parentesis quita el dato que se encuentre en esa posición. Se utiliza si quieres hacerr algo con el elemento eliminado
print(my_list)
print(my_list.pop(1)) #Imprimo el último dato de la lista

del my_list[1] # Elimina el elemento que está en la posición que le indiquemos
print(my_list)

my_new_list = my_list.copy() #Hace una copia de la lista

my_list.clear() #Vacia la lista completa
print(my_list)
print(my_new_list)

my_new_list.reverse() #Da la vuelta a la lista, pero hay que hacerlo antes del print
print(my_new_list)

my_new_list.sort() #Ordena los elementos de la lista
print(my_new_list)

