import pandas as pd
from matplotlib import pyplot as plt

def get_jugadores(data):
    data = data[data['Nombre de evento'] == 'fin']['Usuarie - nick'].value_counts()
    # nombres = data['Usuarie - nick'].value_counts()
    return data

def graficar(etiquetas,jugadores):
    plt.pie(jugadores,labels = etiquetas,autopct="%0.1f %%")
    plt.axis('equal')
    plt.show()

def main():
    data = pd.read_csv('datos de prueba.csv')
    jugadores = get_jugadores(data)
    graficar(jugadores.keys(),jugadores) 
#programa principal
main()