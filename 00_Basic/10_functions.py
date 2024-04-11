
# Funciones simples
def my_function ():
    print('Esto es una funcion')

my_function ()


# Funciones con valores
def sum_two_values (a,b):
    print(a + b)

sum_two_values(5,7)


# Funciones con return
def sum_two_values_with_return (a,b):
     my_sum = a + b
     return (my_sum)

my_result = sum_two_values_with_return (5,17)
print(my_result)


def print_name (name,surname):
    print(f'{name} {surname}')

print_name ('Sanson', 'Nacho')
print_name (surname='Sanson',name= 'Nacho')


def print_name_with_default (name,surname,alias = 'Sin alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default ('Nacho','Sanson','Sansonnnn')  # Nacho Sanson Sansonnnn
print_name_with_default ('Nacho','Sanson')  # Nacho Sanson Sin alias

# Usamos el asterisco cuando no sabemos cuantos argumentos vamos a mandar y los va cogiendo todos.
def print_texts (*text):
    print(text)

print_texts ('Hola','Nacho','Sanson') # ('Hola', 'Nacho', 'Sanson')