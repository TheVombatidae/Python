#1- guardar en otro archivo las peliculas agregadas en el año 2020.
#2- los cinco (5) países con más producciones en Netflix.
import csv
import json
from collections import Counter


def agregadas_2020():
    archivo_csv = open('netflix_titles.csv','r',encoding='UTF-8')
    new_csv = open('agregadas_2020.csv','w',encoding='UTF-8')

    csv_reader = csv.reader(archivo_csv,delimiter = ',')
    csv_writer = csv.writer(new_csv)

    encabezado = csv_reader.__next__()
    csv_writer.writerow(encabezado)

    for line in csv_reader:
        if line[6].endswith('2020'):
            csv_writer.writerow(line)
    archivo_csv.close()
    new_csv.close()


def crear_lista_paises():
    archivo_csv = open('netflix_titles.csv','r',encoding='UTF-8')
    csv_reader = csv.reader(archivo_csv,delimiter = ',')
    csv_reader.__next__()
    paises = []
    for linea in csv_reader:
        pais_linea = linea[5].replace(" ",'').split(',')
        for pais in pais_linea:
            if pais != '':
                paises.append(pais)
    archivo_csv.close()
    return sorted(paises)      


def top_cinco(lista_paises):
    archivo = open('Top_cinco.json','w')
    top_five = Counter(paises)
    dic_top = dict(top_five.most_common(5))
    print('-------PAISES CON MAS PRODUCCIONES------')
    for pais,prod in dic_top.items():
        print(f"Pais: {pais} - Producciones: {prod}")
    json.dump(dic_top,archivo)
    archivo.close()

#close
agregadas_2020()
paises = crear_lista_paises()
top_cinco(paises)


