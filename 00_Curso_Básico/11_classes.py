
class MyEmptyPerson :
    pass # Evita los errores


print(MyEmptyPerson())
print(MyEmptyPerson)


# Los parametros vienen desde fuera
class Person :
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.full_name = f'{name} {surname}'

my_person = Person('Nacho','Sanson')

print(my_person.name)
print(f'{my_person.name} {my_person.surname}')
print(my_person.full_name)

# Los parametros vienen dados dentro del constructor
class Person :
    def __init__(self):
        self.name = 'Nacho'
        self.surname = 'Sanson'
        
my_person = Person()

print(my_person.name)
print(f'{my_person.name} {my_person.surname}')
