
# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=4142

### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for element in range(1,101):
        if element % 3 == 0 and element % 5 == 0:
            print('fizzbuzz')
        elif element % 3 == 0:
            print('fizz')
        elif element % 5 == 0:
            print('buzz')
        else:
            print(element)




fizzbuzz()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    elif sorted(word_one.lower()) == sorted(word_two.lower()):
        return True

print(is_anagram('roma', 'amor'))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():

    prev = 0
    next = 1

    for element in range(0,50):
        print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def is_prime ():
    for number in range(2,101):
            
        is_divisible = False

        for element in range(2,number):
            if number % element == 0:
                 is_divisible = True 
                 break  
        
        if not is_divisible:
            print(number)

is_prime()


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def invert(text):

    reversed_text = ''
    text_len = len(text)

    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(invert('hola mundo'))