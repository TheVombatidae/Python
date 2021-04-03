frase = input("Ingrese frase a codificar: ")
def cifrado_cesar(frase):
    frase_cod = "".join(list(map(lambda char:chr(ord(char)+1),frase)))
    print(frase_cod.replace("!"," "))
    
cifrado_cesar(frase)

