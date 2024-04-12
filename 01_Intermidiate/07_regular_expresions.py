
import re

### Match
my_string = 'Esta es la lección número 7: Lección Expresiones Regulares'
my_other_string = 'Esta no es la lección número 6: Mnaejo de ficheros'

print(re.match('Esta es la lección', my_string))  # <re.Match object; span=(0, 18), match='Esta es la lección'>
print(re.match('Esta es la lección', my_other_string))  # None
print(re.match('Expresiones Regulares', my_string))  # None  No lo reocnoce porque no coincide con el principio de la frase

print(re.match('Esta es la lección', my_string, re.I))  # <re.Match object; span=(0, 18), match='Esta es la lección'>

match = re.match('Esta es la lección', my_string, re.I)
print(match)
start,end = match.span()  # match.span()Te dice entre que caracteres ha encontrado el texto
print(my_string[start:end])  



### Search
search = re.search('Expresiones Regulares', my_string, re.I)
print(search)  #<re.Match object; span=(29, 50), match='Expresiones Regulares'>


### Findall
findall = re.findall('lección', my_string, re.I)
print(findall)  # ['lección', 'Lección']



### Split
split = re.split(':', my_string)
print(split)  # ['Esta es la lección número 7', ' Lección Expresiones Regulares']



### Sub
sub = re.sub('Expresiones', 'EXPRESIONES', my_string)
print(sub)  # Esta es la lección número 7: Lección EXPRESIONES Regulares

sub = re.sub('lección|Lección', 'LECCIÓN', my_string)
print(sub)  # Esta es la LECCIÓN número 7: LECCIÓN Expresiones Regulares


### Patterns

pattern = r'[lL]ección'
print(re.findall(pattern,my_string))  # ['lección', 'Lección']

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern,my_string))  # ['lección', 'Lección', 'Expresiones']

pattern = r'[a-z]'
print(re.findall(pattern,my_string))  # ['s', 't', 'a', 'e', 's', 'l', 'a', 'l', 'e', 'c', 'c', 'i', 'n', 'n', 'm', 'e', 'r', 'o', 'e', 'c', 'c', 'i', 'n', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']

pattern = r'[0-9]'
print(re.findall(pattern,my_string))  # ['7']
print(re.search(pattern,my_string))  # <re.Match object; span=(26, 27), match='7'>

pattern = r'\d' # Saca todos los número pero no las letras
print(re.findall(pattern,my_string))  # ['7']

pattern = r'\D' # Saca todas las letras pero no los numeros
print(re.findall(pattern,my_string))  # ['E', 's', 't', 'a', ' ', 'e', 's', ' ', 'l', 'a', ' ', 'l', 'e', 'c', 'c', 'i', 'ó', 'n', ' ', 'n', 'ú', 'm', 'e', 'r', 'o', ' ', ':', ' ', 'L', 'e', 'c', 'c', 'i', 'ó', 'n', ' ', 'E', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', ' ', 'R', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']