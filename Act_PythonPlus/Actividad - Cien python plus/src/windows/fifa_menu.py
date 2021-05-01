import PySimpleGUI as sg
from src.data import data

def build():
    icono = data.ruta_data('images','futbol-icon.ico')
    "Devuele el la ventana con el layout definido"
    #---estilos---
    color_fondo = "#eeeeee"
    fuente = ('Sans-serif',10,'bold')
    ventana = {'size':(500,300), 'background_color':color_fondo, 'element_justification':'center'}
    botones = {'size':(45,2), 'button_color':'#084405', 'font':fuente,'border_width':3, 'focus':True}
    titulos = {'font':('Arial Black',24), 'background_color':color_fondo, 'text_color':'#1d3fea'}


    # ---Layout---
    layout = [
                [sg.Text(k='-TITULO-', text='FIFA 19', **titulos)],
                [sg.Button(k='-BOT_A-', button_text='20 jugadores con mejor control', pad=((0,0),(10,0)), **botones)],
                [sg.Button(k='-BOT_B-', button_text='10 jugadores argentinos con mejor reputacion', pad=((0,0),(10,0)),**botones)],
                [sg.Button(k='-BOT_C-', button_text='20 jugadores mas caros', pad=((0,0),(10,0)),**botones)],
                [sg.Button(k='-BOT_VOLVER-', button_text='Menu principal', pad=((0,0),(25,0)), **botones)]
            ]

    window = sg.Window('FIFA Menu',layout,**ventana,icon=icono)
    return window