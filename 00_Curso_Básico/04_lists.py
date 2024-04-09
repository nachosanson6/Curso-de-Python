
my_list = list()
my_other_list = [33, 1.78, 'Nacho', 'Sansón']

print(len(my_list))

my_list = [35, 24, 60, 30]
print(my_list)
print(len(my_list))
print(type(my_list))

print(my_list[0])
print(my_list[-1])
print(my_list[-3])
print(my_list.count(24))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

my_list= 'Hola Python'
print(my_list)