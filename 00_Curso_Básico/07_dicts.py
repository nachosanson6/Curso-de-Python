
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