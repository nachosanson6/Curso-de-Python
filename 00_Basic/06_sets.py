 
my_set = set()
my_other_set = {}

print(type(my_set))  #<class 'set'>
print(type(my_other_set))  #<class 'dict'>

my_other_set = {'Nacho', 'Sanson', 33, 1.78}

print(type(my_other_set))  #<class 'set'>
print(len(my_other_set))
print(my_other_set) #Un set no es una estructura ordenada


# Funciones
my_other_set.add('fgdgdf')
print(my_other_set)
my_other_set.add('fgdgdf')
print(my_other_set)  # Si añades dos veces el mismo elemento solo lo almacena 1 sola vez.

print('Sanson' in my_other_set)  # True.  Permite realizar búsquedas
print('Sansin' in my_other_set)  #False

my_other_set.remove(33)  # Permite eliminar el elemento que queramos
print(my_other_set)

my_other_set.clear()  # Vacia el set
print(my_other_set)

del my_other_set  #Elimina el set por completo
#print(my_other_set)

# Se puede transiformar entre list, tuple y set aunque el ordean al pasarlo a lista vairará cada vez que se ejecute

my_set = {'Nacho', 'Sanson', 33}
my_other_set = {'JavaScript', 'React'}
# my_new_set = my_set + my_other_set
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union('node'))  #{'n', 'Nacho', 'JavaScript', 'React', 33, 'Sanson', 'o', 'e', 'd'} NO OLVIDAR LOS CORCHETES
print(my_new_set.union({'node'}))  #{33, 'Nacho', 'Sanson', 'JavaScript', 'node', 'React'}

print(my_new_set.difference(my_set))