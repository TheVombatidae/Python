import PySimpleGUI as sg
from src.data import data

def build(lista):
    icono = data.ruta_data('images','json-icon.ico')

    layout =[
        [sg.Button(k='-BOT_VOLVER-',button_text='Volver',size = (20,1))],
        [sg.Listbox(k='LISTBOX_DATA',values=lista,text_color='#f1f1f1',background_color='#714e8b',size=(800,300),font=('Consolas',9))]
    ]

    window = sg.Window('Visor JSON',layout,size=(800,300),background_color='#252525',icon=icono)
    return window