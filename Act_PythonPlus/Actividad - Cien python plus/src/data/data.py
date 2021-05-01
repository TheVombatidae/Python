import json
import csv
import os

def ruta_data(carpeta,archivo):
    """Devuelve la ruta absoluta de un directorio y archivo(si el directorio no existe lo crea)"""
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_carpeta = os.path.join(ruta_base,carpeta)
    if not os.path.isdir(ruta_carpeta):
        os.mkdir(ruta_carpeta)
        return True
    ruta_final = os.path.join(ruta_carpeta,archivo)
    return ruta_final

def archivo_json_existe(name):
    """Retorna True si existe el archivo 'x.json' en el directorio ../json/"""
    ruta_archivo = ruta_data('json',name)
    return True if os.path.isfile(ruta_archivo) else False
        
def convertir_csv_a_json(file_csv,json_name):
    """crea un archivo json a partir de un archivo csv utilizando DictReader,
    si el archivo ya existe retorna None"""
    ruta_csv = ruta_data('csv',file_csv) #defino ruta en la que buscar el archivo csv
    ruta_json = ruta_data('json',json_name)  #defino ruta en la que guardar el archivo json()
    #si el archivo json no existe lo creo
    if not archivo_json_existe(json_name):
        if os.path.exists(ruta_csv):
            try:
                with open(ruta_csv,'r',encoding='UTF-8') as file_csv:          
                    lector = csv.DictReader(file_csv)
                    data,id= {},0
                    for fila in lector:
                        if '' in fila:
                            fila.pop('')
                        data[id] = fila
                        id+=1
                try:
                    with open(ruta_json,'w') as file_json:
                        file_json.write(json.dumps(data,indent=4))
                except:
                    print('Algo salio mal al crear el archivo json')
            except:
                print('Algo salio mal al leer el archivo csv')
        else:
            print('Error al intentar encontrar la ruta')
    else:
        return None

