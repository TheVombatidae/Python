#Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada
#la siguiente tabla de valores del juego Scrabble:
#Letra valor
#A, E, I, O, U, L, N, R, S, T - 1
#D, G  - 2
#B, C, M, P - 3
#F, H, V, W, Y - 4
#K  - 5
#J, X  - 8
#Q, Z - 10


tabla = {
1:('A','E','I','O','U','L','N','R','S','T'),
2:('D','G'),
3:('B','C','M','P'),
4:('F','H','V','W','Y'),
5:('K', ),
8:('J','X'),
10:('Q','Z')
}

#lista con las claves del diccionario
#claves = list(tabla.keys())

palabra = input("Ingres palabra: ").upper()
p = [c for c in palabra if palabra.isalpha()]
pts = 0


#for c in p:   
#    for key in tabla: 
#         if c in tabla[key]:
#             pts = pts + key
#             break 

for c in p:
    for k,l in tabla.items():
        if c in l:
            pts = pts + k
            break

print("La plabra '"+palabra.capitalize()+f"' vale {pts} puntos"  )