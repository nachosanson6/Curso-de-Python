 
my_set = set()
my_other_set = {}

print(type(my_set))  #<class 'set'>
print(type(my_other_set))  #<class 'dict'>

my_other_set = {'Nacho', 'Sanson', 33, 1.78}

print(type(my_other_set))  #<class 'set'>
print(len(my_other_set))
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add('fgdgdf')
print(my_other_set)
my_other_set.add('fgdgdf')
print(my_other_set)  # Si añades dos veces el mismo elemento solo lo almacena 1 sola vez.