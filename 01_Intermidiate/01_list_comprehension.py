

my_original_list = [0, 1, 2, 3, 4, 5, 6]
print(my_original_list)  # [0, 1, 2, 3, 4, 5, 6]

my_range=range(7) # Crea una lista desee el 0 al 6
print(list(my_range))  # [0, 1, 2, 3, 4, 5, 6]

my_list = [i for i in range(7)] # Crea una lista desee el 0 al 6
print(my_list)   # [0, 1, 2, 3, 4, 5, 6]

my_list = [i + 1 for i in range(7)] # Crea una lista de los números del 0 al 6 sumandole 1
print(my_list)  # [1, 2, 3, 4, 5, 6, 7]

my_list = [i * 2 for i in range(7)] # Crea una lista con el doble de los números desde el 0 al 6
print(my_list)  # [0, 2, 4, 6, 8, 10, 12]


def sum_five(number):
    return number +5 

my_list = [sum_five(i) for i in range(7)] # Crea una lista de los números del 0 al 6 sumandole 5
print(my_list)  # [5, 6, 7, 8, 9, 10, 11]


