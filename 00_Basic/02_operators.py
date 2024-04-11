### Operadores artiméticos ###
print('Suma:',3 + 2)
print('Resta:',3 - 2)
print('Multiplicación:',3 * 2)
print('Exponente:',3 ** 2)
print('División:',3 / 2)
print('División aproximada a un número entero:',3 // 2)
print('Resto:',3 % 2)

print('Hola ' + 'Python')
print('Hola ' * 5)

### Operadores comparativos ###
print('')
print(3 < 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3  != 4)

#Compara el roden albatético, para comparar el número de caracteres tenemos que comparar len('hola')
print('')
print('Hola' < 'Python')
print('Hola' > 'Python')
print('Hola' <= 'Python')
print('Hola' >= 'Python')
print('Hola' == 'Hola')
print('Hola'  != 'Python')

### Operadores lógicos ###
print('')
print(3 > 4 and 'hola' > 'python') # Los dos true
print(3 > 4 or 'hola' > 'python') # Uno de los dos true
print(3 < 4 and 'hola' < 'python')
print(3 < 4 or 'hola' > 'python')
print(not(3>4)) # Revierte el true o false
