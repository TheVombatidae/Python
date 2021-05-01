import PySimpleGUI as sg
from src.windows import fifa_menu
from src.handlers import fifa,info
from src.components import informacion

def start():
    window = loop()
    window.close()


def loop():
    """fifa-menu loop"""
    window = fifa_menu.build()
    while True:
        event,_values = window.read()
        if event in (sg.WIN_CLOSED,'-BOT_VOLVER-'):
            break
        if event == '-BOT_A-':  #20 jugadores con mejor control
            display('a','jug_controladores.json','control',window)
            # fifa.jugadores_estadisticas()
        if event == '-BOT_B-':  #10 jugadores argentinos con mejor reputacion
            display('b','jug_reputacion.json','reputacion',window)
            # fifa.jugadores_estadisticas('b','reputacion','jug_reputacion.json')
        if event == '-BOT_C-':  #20 jugadores mas caros
            display('c','jug_caros.json','precio',window)
            # fifa.jugadores_estadisticas('c','precio','jug_caros.json')

    return window

def display(*args):
    limite = len(args) - 1
    window,data = args[limite],args[:limite]
    fifa.jugadores_estadisticas(data)
    window.hide()
    lista = info.obtener_lista(args[1]) #args 1 = nombre del archivo json
    informacion.start(lista)
    window.un_hide()