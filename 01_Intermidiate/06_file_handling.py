
import os
### .txt files

text_file = open('01_Intermidiate/my_file.txt','r+')  # r+ para leer y escribir/ w+ para leer, escribir y sobreescribirlo

#text_file.write('Mi nombre es Nacho\nMi apellido es Sanson \nMi edad es 33 años\n Mi lenguaje favorito es React')

# print(text_file.read())  # Se imprimer todo el texto
#print(text_file.read(15))  # Mi nombre es Na
#print(text_file.readline())  # Mi nombre es Nacho
#print(text_file.readline())  # Mi apellido es Sanson
#print(text_file.readlines())  # ['Mi nombre es Nacho\n', 'Mi apellido es Sanson\n', 'Mi edad es 33 aÃ±os\n', 'Mi lenguaje favorito es React']
for line in text_file.readlines():
        print(line) # Mi nombre es Nacho Mi apellido es Sanson Mi edad es 33 aÃ±os Mi lenguaje favorito es React


text_file.write('\nAunque tambien me gusta python')
print(text_file.readline())

#text_file.close()

with open('01_Intermidiate/my_file.txt','a') as my_other_file:
     my_other_file.write('\nY Swift')

# os.remove('01_Intermidiate/my_file.txt')  @ Elimina el archivo



### .json files

import json

json_file = open('01_Intermidiate/my_json.json','w+')
json_test = {
        'Nombre':'Nacho',
        'Apellido': 'Sanson',
        'Edad': 33,
        'languages' :[ 'React ','javascript','node']
}
json.dump(json_test,json_file,indent=0)  # Escribir en la json
json_file.close()

with open('01_Intermidiate/my_json.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open('01_Intermidiate/my_json.json'))
print(json_dict)
print(type(json_dict))


### .csv files

import csv

csv_file = open('01_Intermidiate/my_file.csv','w+')

csv_write = csv.writer(csv_file)
csv_write.writerow(['name','surname','age','language'])
csv_write.writerow(['nacho','sanson','33','react'])
csv_write.writerow(['nuria','soriano','30','python'])

csv_file.close()

with open('01_Intermidiate/my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)



### .xml files

import xml