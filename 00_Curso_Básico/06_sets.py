 
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

