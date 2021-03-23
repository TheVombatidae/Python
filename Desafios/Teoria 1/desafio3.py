letra = input("ingrese una letra ")

if letra >= "a" and letra <= "z":
	print(letra + " es minuscula")
elif letra >= "A" and letra <= "Z":
	print(letra + " es mayuscula")
else:
	print("El caracter ingresado no es una letra")
