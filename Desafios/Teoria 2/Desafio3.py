#Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:
#• cuál es el promedio de las notas;
#• cuántos estudiantes están por debajo del promedio.

#Ingresar notas, cargo lista, calculo promedio ->

lista_notas = []

nota = int(input("Ingrese una nota(-1 para finalizar):  "))
while nota != -1:
    lista_notas.append(nota)
    nota = int(input("Ingrese una nota(-1 para finalizar):  "))
promedio = sum(lista_notas) / len(lista_notas)

#Recorro la lista y calculo cuantos superan el promedio ->

cant_menores = 0

for n in lista_notas:
    if n < promedio:
        cant_menores += 1

print(f"\nEl promedio es: {promedio}")
print("---------------------------")
print(f"La cantidad de alumnos que no supera el promedio son {cant_menores}")
