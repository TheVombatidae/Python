import pandas as pd
from wordcloud import WordCloud, wordcloud
import matplotlib.pyplot as plt

def lista_palabras():
    archivo = 'Pokemon.csv'
    df = pd.read_csv(archivo,encoding='UTF-8')
    new_df = df[(df["Type 1"] == "Fire") | (df["Type 1"] == "Flying")]
    return new_df['Name']

text = str(lista_palabras())

wordcloud = WordCloud(width = 800, height = 600,background_color='white', colormap='RdPu', collocations=True).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()