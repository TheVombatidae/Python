#5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras,
#y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir
#entre mayúsculas y minúsculas.

frase = input("Ingrese una frase: ")
palabras = frase.lower().split(" ")
palabra = input("Ingrese una palabra: ")
palabra.lower()

print("Cantidad de veces que aparece: " , palabras.count(palabra))


