my_string = 'my string'
my_other_string = 'my other string'

print(len(my_string))
print(len(my_other_string))
print(my_string, 'and', my_other_string)

my_new_line_string = 'Este esu n string\ncon salta de linea'
print(my_new_line_string)

my_new_tab_string = 'Este esu n string\tcon salta de linea'
print(my_new_tab_string)

#Formateo
name = 'Nacho'
surname = 'Sansón'
age = 33

print('Mi nombre es {} {} y mi edad es {}'.format(name,surname,age))
print('Mi nombre es %s %s y mi edad es %d' %(name,surname,age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

#Desempaquetado de caracteres
'''language = 'Python'
a , b = language
print(a)
print(b)'''

language = 'Python'
a , b, c, d, e, f = language
print(a)
print(b)

#División

language_slice = language[1:4]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#Reverse

reversed_language = language[:: -1] #Da la vuelta a la palabra
print(reversed_language)

#Funciones
print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.lower())
print(language.upper().isupper())