import PySimpleGUI as sg
from src.components import informacion
from src.windows import games_menu
from src.handlers import games,info

def start():
    window = loop()
    window.close()


def loop():
    """Games-Menu loop"""
    window = games_menu.build()
    while True:
        event,_values = window.read()
        if event in (sg.WIN_CLOSED,'-BOT_VOLVER-'):
            break
        if event == '-BOT_A-':
            display('a','ventas_nintendo.json','Ventas',20,window)
        if event == '-BOT_B-':
            display('b','critcas_nintendo_pc.json','Critica',10,window)
        if event == '-BOT_C-':
            display('c','ventas_sports_NA.json','Ventas',5,window)
    return window

def display(*args):
    window,data = args[4],args[:4]
    games.games_estadisticas(data)
    window.hide()
    lista = info.obtener_lista(args[1]) #args 1 = nombre del archivo json
    informacion.start(lista)
    window.un_hide()