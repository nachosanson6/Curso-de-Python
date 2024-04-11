
# from 10_functions import sum_two_values  NO ACEPTA ARCHIVOS QUE EMPIEZAN POR NUMERO

# Importamos el archivo entero.
import module

module.sum_values(4, 5, 6)
module.printValue('hola')


# Importamos las funciones por separadas
from module import sum_values, printValue

sum_values(5, 2, 9)
printValue('hola')