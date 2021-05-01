import PySimpleGUI as sg
from src.data import data

def build():
    icono = data.ruta_data('images','main-icon.ico')

    "Devuele la ventana con el layout definido"
    #---estilos---
    color_fondo = "#3a064d"
    fuente = ('Calibri',10)
    ventana = {'size':(300,200), 'background_color':color_fondo, 'element_justification':'center'}
    botones = {'size':(15,1), 'button_color':'#cb0f42', 'font':fuente,'border_width':3, 'focus':True}
    titulos = {'font':('Arial Black',15), 'background_color':color_fondo, 'text_color':'#ffffff'}
    barra = {'max_value':1000,'visible':False,'size':(400,10),'pad':((0,0),(15,0))}


    # ---Layout---
    layout = [
                [sg.Text(k='-TITULO-', text='Analisis de datos', **titulos)],
                [sg.Button(k='-BOT_FIFA-', button_text='Jugadores de FIFA', pad=((0,0),(10,0)), **botones)],
                [sg.Button(k='-BOT_JUEGOS-', button_text='Videojuegos', pad=((0,0),(10,0)),**botones)],
                [sg.Button(k='-BOT_SALIR-', button_text='Salir', pad=((0,0),(25,0)), **botones)],
                [sg.ProgressBar(k='-STATUS_BAR-',**barra)]
            ]

    window = sg.Window('Menu',layout,**ventana,icon=icono)
    return window

def loading(window):
    """Actualiza la ventana a modo de 'carga'"""
    window['-BOT_SALIR-'].update(disabled = True)
    for i in range(1000):
        event, _values=window.read(timeout = 1)
        if event == sg.WIN_CLOSED:
            return False
        window['-STATUS_BAR-'].update(i+1,visible=True)
    return True

def restore_menu(window):
    """Restablece el menu al estado original"""
    window['-BOT_SALIR-'].update(disabled = False)
    window['-STATUS_BAR-'].update(0,visible = False)