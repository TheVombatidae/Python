#Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
#aquellas que empiecen y terminen con la misma letra.

palabra = input("Ingrese una palabra:  ")
while "FIN" not in palabra:
    if palabra.startswith(palabra[0]) == palabra.endswith(palabra[0]):
        print("La palabra: " + palabra + " empieza y termina con la misma letra")
    palabra = input("Ingrese una palabra:  ")
