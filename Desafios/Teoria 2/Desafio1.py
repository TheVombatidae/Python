#Modificar el código anterior para que se imprima la cadena “TIENE R” si la
#palabra contiene la letra r y sino, imprima “NO TIENE R”.

for i in range(4):
    palabra = input("Ingrese una palabra:  ")
    msj = "Tiene R" if "r" in palabra else "No tiene R"
    print(msj)
