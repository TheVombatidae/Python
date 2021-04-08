import Listas
def cargar_alumnos(i):
    """Retorna diccionario con los datos del alumno""" 
    dic = dict(nombre= Listas.nombre[i].capitalize(),nota_1= int(Listas.eva1[i]),
     nota_2= int(Listas.eva2[i]), nota_final= int(Listas.eva1[i]) + int(Listas.eva2[i]))
    return dic

def calc_prom_gral(lista_alu):
    "Retorna una cadena con la suma y el promedio de notas"
    suma = (sum(alum.get('nota_final') for alum in lista_alu))
    promedio = suma / len(lista_alu)
    cad = f"Suma nota finales = {suma}  /  Promedio general = {round(promedio,2)}"
    return cad

def imprimir_listado(lista_alu):
    formato = "{:10} {:6} {:6} {:5}"  
    print(formato.format('Nombre','Nota 1','Nota 2','Nota final'))
    print(formato.format('------','------','------','--------'))
    for alu in lista_alu:
        print(formato.format(alu['nombre'],alu['nota_1'],alu['nota_2'],alu['nota_final']))
    print(formato.format('------','------','------','--------'))

def leer_rango(opc):
    ok = False
    if opc == 'a' or 'b':
        rango = range(1,100)
        ok = True
    elif opc == 'c':
        rango = range(1,200)
        ok = True
    if ok:
        r_min = int(input('Ingrese rango minimo'))
        if r_min in rango:
            r_max = int(input('Ingrese rango maximo'))
            if r_max in rango and r_max > r_min:
                return range(r_min,r_max)