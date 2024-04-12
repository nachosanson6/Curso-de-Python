
### SintaxError 
# print 'Hola mundo!' # Descomentar para Error  Le faltan las comillas al print
print ('Hola mundo!')



### NameError  
name='nacho'  # Comentar para Error
print(name)  # La variable no está definida



### IndexError
my_list =['python','javascript','node','react']
print(my_list[1]) # Cambiar indice a número superior a 3 para Error



### ModuleNotFoundError
# import maths  # Descomentar para Error
import math



### AttributeError
print(math.pi)  # Cambiar pi a mayusculas para Error



### KeyError
my_dict = {'Nombre':'Nacho', 'Apellido': 'Sanson', 'Edad': 33, 1 : 'React '}
print(my_dict['Edad'])  # Cambiar Edad por edad para Error



### TypeError  
# print(my_list['Nombre'])  # Descomentar para Error



### ImportError
from math import pi  # Cambiar pi por PI para Error



# ValueError
# my_int = int('10 Años') # Descomentar para Error




#ZeroDivisionError
# print(4/0)  # Descomentar para Error
