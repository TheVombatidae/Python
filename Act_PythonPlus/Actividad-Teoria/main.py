"""# Ayuda para el punto 2
import requests

juego = "Sudoku"
icon_url = "https://is2-ssl.mzstatic.com/image/thumb/Purple127/v4/7d/23/c6/7d23c660-aba8-308a-05c0-19385a377c0e/source/512x512bb.jpg"
icono = requests.get(icon_url)
with open(f'ejemplos/clase6/{juego}.jpg', 'wb') as f:
    f.write(icono.content)"""

import csv
from collections import Counter
import operator

#-------------------PUNTO 1-----------------------------
def listar_esp():
    lista_gratis_esp = []
    with open('appstore_games.csv','r',encoding='UTF-8') as archivo:
        reader = csv.reader(archivo,delimiter=',')
        reader.__next__() #Ignorar encabezado
        for line in reader:
            if line[7] == '0': #si precio es 0
                lista_paises = line[12].replace(' ','').split(',')
                if 'ES' in lista_paises:#si ES en lista paises
                    lista_gratis_esp.append(line[2]) #Agrego nombre
    return lista_gratis_esp


#-----------------------PUNTO 2-------------------------

def diez_mejores():
    diez_mej = []
    with open('appstore_games.csv','r',encoding='UTF-8') as archivo:
        reader = csv.reader(archivo,delimiter=',')
        reader.__next__() #Ignorar encabezado
        dic = {}
        for line in reader:
            if line[6] != '':
                dic[line[4]] = int(line[6]) #4 = url / 6 = valoracion

    dic = sorted(dic.items(), key=operator.itemgetter(1)) #ordeno por clave
    # cont = 0
    # for i in reversed(range(len(dic))):
    #     if cont == 10:
    #         break
    #     diez_mej.append(dic[i])
    #     cont +=1
 
    diez_mej = [dic[i] for i in reversed(range(len(dic))) if i >= len(dic)-10] # diez mejores list comprehension
    return diez_mej

print('----------------------------PUNTO 1------------------------------------')
print(listar_esp())
print('-----------------------------------------------------------------------')

print('----------------------------PUNTO 2------------------------------------')
print(diez_mejores())
print('-----------------------------------------------------------------------')


