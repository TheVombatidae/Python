import PySimpleGUI as sg
from src.components import fifa_menu,games_menu
from src.data import data
from src.windows import menu

def start():
    """Ejecuta el loop del menu"""
    window = loop()
    window.close()

def loop():
    """Menu loop"""
    data.ruta_data('json','')
    window = menu.build()
    while True:
        event, _values = window.read()
        if event in (sg.WIN_CLOSED,'-BOT_SALIR-'):
            break

        if event == '-BOT_FIFA-':
            inicializar(('data_fifa.json','data_fifa.csv',window),fifa_menu)
        if event == '-BOT_JUEGOS-':
            inicializar(('video_juegos.json','video_juegos.csv',window),games_menu)            
    return window

def inicializar(datos,funcion):
    """Verifica si el archvio json existe sino lo crea e inicializa el siguiente menu"""
    archivo_json,archivo_csv,window = datos
    if not data.archivo_json_existe(archivo_json):
        if menu.loading(window):
            data.convertir_csv_a_json(archivo_csv,archivo_json)
            menu.restore_menu(window)
    window.hide()
    funcion.start()
    window.un_hide()
