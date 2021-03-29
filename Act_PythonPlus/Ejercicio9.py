#9. Escbriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
#misma es un Heterograma

palabra = input("Ingrese una palabra o frase para identificar si es un heterograma: ").lower()
p = palabra.replace(' ','')

car = [c for c in p if c.isalpha()]
car_unicos = list(set(car))
if(len(car) == len(car_unicos)):
    print("La palabra o frase '" + palabra.capitalize() + "' es un heterograma")
else:
    print("La palabra o frase ingresada no es un heterograma")