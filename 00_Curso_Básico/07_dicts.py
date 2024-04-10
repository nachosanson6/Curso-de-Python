
my_dict = dict()
my_other_dict = {}

my_other_dict = {'Nombre':'Nacho', 'Apellido': 'Sanson', 'Edad': 33, 1 : 'React '}
print(my_other_dict)  # {'Nombre': 'Nacho', 'Apellido': 'Sanson', 'Edad': 33, 1: 'React '}

my_dict = {
    'Nombre':'Nacho',
    'Apellido':'Sanson',
    'Edad':33,
    'Lenguajes': {'React','Javascript','Node'},
    1: 'hola'
}

print(my_dict)  # {'Nombre': 'Nacho', 'Apellido': 'Sanson', 'Edad': 33, 'Lenguajes': {'Node', 'React', 'Javascript'}}
print(len(my_dict))  # 4
print(my_dict['Nombre'])  # Nacho
print(my_dict['Lenguajes'])  # {'Node', 'Javascript', 'React'}

my_dict['Nombre'] = 'Nuria'  # Se pueden cambiar los valores de la clave que elijamos
print(my_dict)

my_dict['Calle'] = 'Santa Genoveva'  #Se pueden añadir nuevas claves
print(my_dict)

# Funciones
# Dos maneras de eliminar una clave
my_dict.pop(1) 
print (my_dict)
del my_dict['Calle']
print(my_dict)

print('Apellido' in my_dict)  # True. Busca por clave no por valor
print('Sanson' in my_dict)  #False

print(my_dict.items())  # dict_items([('Nombre', 'Nuria'), ('Apellido', 'Sanson'), ('Edad', 33), ('Lenguajes', {'React', 'Javascript', 'Node'})])
print(my_dict.keys())  # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes'])
print(my_dict.values())  # dict_values(['Nuria', 'Sanson', 33, {'React', 'Javascript', 'Node'}])

my_new_dict = my_dict.fromkeys(('Nombre', 'Apellido')) # Crea un nuevo diccionario con esas clasves pero sin valores
print(my_new_dict) # {'Nombre': None, 'Apellido': None}

my_new_dict = dict.fromkeys(('Nombre', 'Apellido','Piso')) # Crea un nuevo diccionario con esas clasves pero sin valores
print(my_new_dict)  # {'Nombre': None, 'Apellido': None, 'Piso': None}

my_new_dict = dict.fromkeys(my_dict) # Crea un nuevo diccionario con las claves del anterior dict pero con los valores vacios
print(my_new_dict)  # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None}

# Con el segundo valor de fromkey añade ese segundo valor a cada una de las claves

my_new_dict = dict.fromkeys(my_dict, ('Nacho','Sanson')) # 
print(my_new_dict)  # {'Nombre': ('Nacho', 'Sanson'), 'Apellido': ('Nacho', 'Sanson'), 'Edad': ('Nacho', 'Sanson'), 'Lenguajes': ('Nacho', 'Sanson')}

my_new_dict = dict.fromkeys(my_dict, ['Nacho','Sanson']) # 
print(my_new_dict)  # {'Nombre': ['Nacho', 'Sanson'], 'Apellido': ['Nacho', 'Sanson'], 'Edad': ['Nacho', 'Sanson'], 'Lenguajes': ['Nacho', 'Sanson']}

my_new_dict = dict.fromkeys(my_dict, ['Nacho','Sanson']) # 
print(my_new_dict)  #