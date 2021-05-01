from src.data import data
import json

def obtener_lista(nom_json):
    ruta_json = data.ruta_data('json',nom_json)
    try:
        with open(ruta_json,'r') as file:
            info = json.load(file)
    except FileNotFoundError: print('Error al intentar leer el archivo')
    return info
