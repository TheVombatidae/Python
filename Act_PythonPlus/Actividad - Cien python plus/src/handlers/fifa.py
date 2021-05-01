import os
import json
from src.data import data

def jugadores_estadisticas(datos):
    """Almacena en un archivo json los datos seleccionados"""
    button, nombre_json, clave = datos
    if not data.archivo_json_existe(nombre_json): #verifico el archivo de estadisticas no esta creado
        try:
            ruta_data_json = data.ruta_data('json','data_fifa.json')
            with open(ruta_data_json,'r') as file:
                dic = json.load(file)
            lista = crear_datos(dic,clave,button)
            try:
                with open(data.ruta_data('json',nombre_json),'w') as file:
                    file.write(json.dumps(lista,indent=4))
            except:
                print(f'Algo salio mal al intentar crear el archivo json')
        except:
            print(f'Algo ocurrio al intentar abrir el archivo json -> {ruta_data_json}')
    else:return None

def crear_datos(*args):
    """Retorna una lista segun la opcion seleccionada"""
    dic,clave,button = args
    lista = []
    for elem,valor in dic.items():
        try:
            if button == 'a':
                v = int(valor['BallControl'])
            elif button == 'b':
                if valor['Nationality'] == 'Argentina':
                    v = int(valor['International Reputation'])
                else: continue
            else: v = definir_precio(valor['Value'])
        except ValueError:pass
        player = {'ID':elem,'nombre':valor['Name'],clave:v}
        lista.append(player)
    cant = 20 if button != 'b' else 10
    lista = sorted(lista,key = lambda p:p[clave],reverse=True)
    return lista[:cant]

def definir_precio(valor):
    """Recibe un valor,remplaza determinados caracteres, lo transforma en float y lo devuelve"""
    valor = valor.replace('€','')
    valor = float(valor.replace('M','')) * 1000000  if valor.endswith('M') else float(valor.replace('K','')) * 1000
    return valor





