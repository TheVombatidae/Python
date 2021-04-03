def imprimir_tipo(*args):
    #Docstring
    """Imprime los argumentos y sus tipos"""
    for valor in args:
        print(f"{valor} es del tipo {type(valor)}")

imprimir_tipo("hola",12,[1,2,3],(9, ),29.56)