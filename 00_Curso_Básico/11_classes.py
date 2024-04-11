
class MyEmptyPerson :
    pass # Evita los errores


print(MyEmptyPerson())
print(MyEmptyPerson)

# Los parametros vienen dados dentro del constructor
class Person :
    def __init__(self):
        self.name = 'Nacho'
        self.surname = 'Sanson'
        
my_person = Person()

print(my_person.name)
print(f'{my_person.name} {my_person.surname}')


# Los parametros vienen desde fuera
class Person :
    def __init__(self,name,surname,alias = 'Sin alias'):
        self.__name = name  # Con las dos barras bajas privatizo este dato y no se puede acceder a él
        self.__surname = surname
        self.alias = alias
        self.full_name = f'{name} {surname} {alias}'

    def get_name (self):
        return self.__name
    
    def walk(self):
        print(f'{self.full_name} está caminando')

my_person = Person('Nuria','Soriano')

# print(my_person.name)
# print(f'{my_person.name} {my_person.surname}')
print(my_person.full_name)
my_person.walk()
print(my_person.get_name())





