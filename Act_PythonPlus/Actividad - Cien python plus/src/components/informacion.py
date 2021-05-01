import PySimpleGUI as sg
from src.windows import informacion

def start(lista):
    window = loop(lista)
    window.close()


def loop(lista):
    """Informacion loop"""
    window = informacion.build(lista)
    while True:
        event,_values = window.read()
        if event in (sg.WIN_CLOSED,'-BOT_VOLVER-'):
            break

    return window