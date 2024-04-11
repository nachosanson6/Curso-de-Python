
number_one = 5
number_two = '2'

try:
    print(number_one + number_two)

except:
    print('Se ha producido un error')

else: # Opcional
    # Se ejecuta si no hay un error
    print('La ejecución continúa')

finally: # Opcional
        # Se ejecuta siempre
        print('La ejecución continúaaaaaa')


# Errores por tipo
try:
    print(number_one + number_two)
    
except ValueError:
    print('Se ha producido un ValuError')

except TypeError: # Solo se ejecuta si el error es por tipo, si se produce otro tipo de error, se rompe
    print('Se ha producido un TypeError')
