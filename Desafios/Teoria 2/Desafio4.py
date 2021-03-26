#Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:
#- cuál es el promedio de las notas
#- qué estudiantes están por debajo del promedio.
#Ingresando nombres ->

#Modularizando
#Ingreso nombre y notas y cargo el diccionario:
def ingreso_notas():
    nom = input("Ingrese nombre del alumno(FIN para finalizar):  ")
    diccionario = {} #vacio
    while(nom != 'FIN'):
        nota = int(input("Ingrese nota del alumno: "))
        diccionario[nom] = nota
        nom = input("Ingrese nombre del alumno(FIN para finalizar):  ")
    return diccionario

#suma valores del diccionario / cant elementos:
def promedio_estudiantes(diccionario):
    prom = sum(diccionario.values()) / len(diccionario)
    print(f"El promedio de las notas es: {prom}\n" + "ALUMNOS POR DEBAJO DEL PROMEDIO\n")
    for elem in diccionario:
        if(diccionario[elem] < prom):
            print("Nombre del alumno: " , elem , "\nNota del alumno: " , diccionario[elem])

#Invoco las funciones:
promedio_estudiantes(ingreso_notas())