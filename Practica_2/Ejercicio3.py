#3. Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
#letra. En caso que no se haya inrgesado un letra, indique el error. Ver: módulo string

texto = """Lorem ipsum dolor sit amet consectetur langostino lambda adipiscing elit duis habitasse hendrerit, vulputate scelerisque ultricies id hac praesent platea maecenas."""

palabras = texto.replace(","," ").split(" ")
letra = input("Ingrese una letra: ")

if(letra.isalpha()):
    for p in palabras:
        if(p.startswith(letra)):
            print(p)
else:
    print("El caracter ingresa no es una letra")
