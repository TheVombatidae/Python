import PySimpleGUI as sg
from src.data import data

def build():
    icono = data.ruta_data('images','pad-icon.ico')

    "Devuele el la ventana con el layout definido"
    #---estilos---
    color_fondo = "#fb8c00"
    fuente = ('Calibri',10,'bold')
    ventana = {'size':(500,400), 'background_color':color_fondo, 'element_justification':'center'}
    botones = {'size':(45,3), 'button_color':'#1b5e20', 'font':fuente,'border_width':3, 'focus':True}
    titulos = {'font':('Arial Black',20,), 'background_color':color_fondo, 'text_color':'#17202a'}


    # ---Layout---
    layout = [
                [sg.Text(k='-TITULO-', text='JUEGOS', **titulos)],
                [sg.Button(k='-BOT_A-', button_text='20 juegos con mas ventas en NINTENDO DS', pad=((0,0),(10,0)), **botones)],
                [sg.Button(k='-BOT_B-', button_text='10 juegos con mejores criticas en PC (2010)', pad=((0,0),(10,0)), **botones)],
                [sg.Button(k='-BOT_C-', button_text='5 juegos de deportes mas vendidos en Norte America', pad=((0,0),(10,0)), **botones)],
                [sg.Button(k='-BOT_VOLVER-', button_text='Menu Principal', pad=((0,0),(35,0)), **botones)],
            ]

    window = sg.Window('Games Menu',layout,**ventana,icon=icono)
    return window