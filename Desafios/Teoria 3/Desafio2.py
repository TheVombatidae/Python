def ordenar(cad):
    """Ordena las palabras de una frase en orden alfabetico"""
    palabras = cad.split()
    #palabras.sort(key=str.lower)
    #return palabras

    #otra forma
    return sorted(palabras, key=str.lower)

print(ordenar("Probando la funcion ordenar para el desafio 2"))