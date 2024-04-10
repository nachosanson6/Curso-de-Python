
my_loop_condition = 0

# While

while my_loop_condition < 10:
    print(my_loop_condition)
    my_loop_condition += 1
else: print('Se acabo')


# For

my_list = [1,2,3,4,5,6,7]

for element in my_list:
    print(element) # 1, 2, 3, 4, 5, 6, 7

    
my_tuple = (50, 90, 25, 84)
for element in my_tuple:
    print(element)  # 50, 90, 25, 84

my_set = {'Nacho', 'Sanson', 33}
for element in my_set:
    print(element)  # 33, Nacho, Sanson

my_dict = {
    'Nombre':'Nacho',
    'Apellido':'Sanson',
    'Edad':33,
    'Lenguajes': {'React','Javascript','Node'},
    1: 'hola'
}
for element in my_dict:
    print(element)  # Nombre, Apellido, Edad, Lenguajes, 1
