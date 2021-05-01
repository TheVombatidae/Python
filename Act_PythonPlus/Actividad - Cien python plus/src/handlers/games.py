import json
import os
from src.data import data

def games_estadisticas(datos):
    button,nombre_json,orden_key,cant = datos
    if not os.path.isfile(data.ruta_data('json', nombre_json)):
        try:
            ruta_data_games = data.ruta_data('json','video_juegos.json')
            with open(ruta_data_games,'r') as file:
                dic = json.load(file)
            
            juegos = []
            for i,valor in dic.items(): 
                if button == 'a': #juegos de nintendo DS con mas ventas globales
                    if valor['Publisher'] == 'Nintendo' and valor['Platform'] == 'DS':
                        juegos.append(dict(ID=i,Nombre=valor['Name'],Ventas=float(valor['Global_Sales'])))
                elif button == 'b': #juegos de pc con mejores criticas en el 2010
                    if valor['Platform'] == 'PC' and valor['Year_of_Release'] == '2010':
                        if not valor['Critic_Score'] == '':
                            juegos.append(dict(ID=i,nombre=valor['Name'],Critica=int(valor['Critic_Score'])))  
                else:# 5 juegos de deportes mas vendidos en Norte America
                     if valor['Genre'] == 'Sports':
                         juegos.append(dict(ID=i,Nombre=valor['Name'],Ventas=float(valor['NA_Sales'])))

            juegos=sorted(juegos,key=lambda juego:juego[orden_key],reverse=True)
            
            #Escribo el archivo en /data/json/'nombre_json'.json
            try:
                with open(data.ruta_data('json',nombre_json),mode='w') as file:
                    file.write(json.dumps(juegos[:cant],indent=2))
            except:
                print(f'Error al escribir el archivo {nombre_json}')      
        except FileNotFoundError:
            print('Error al encontrar el archivo video_juegos.json')
            


