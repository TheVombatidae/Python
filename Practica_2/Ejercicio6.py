#

frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás
que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda
y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos
con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una"""

lista_palabras = frase.replace("."," ").lower().split(" ")
lista = []

for p in lista_palabras:
    if p not in lista:
        lista.append(p)

lista.sort()
print(lista)
