nombre = """"Agustin",
    "Alan",
    "Andrés",
    "Ariadna",
    "Bautista",
    "CAROLINA",
    "CESAR",
    "David",
    "Diego",
    "Dolores",
    "DYLAN",
    "ELIANA",
    "Emanuel",
    "Fabián",
    "Facundo",
    "Facundo",
    "FEDERICO",
    "FEDERICO",
    "GONZALO",
    "Gregorio",
    "Ignacio",
    "Jonathan",
    "Jonathan",
    "Jorge",
    "JOSE",
    "JUAN",
    "Juan",
    "Juan",
    "Julian",
    "Julieta",
    "LAUTARO",
    "Leonel",
    "LUIS",
    "Luis",
    "Marcos",
    "María",
    "MATEO",
    "Matias",
    "Nicolás",
    "NICOLÁS",
    "Noelia",
    "Pablo",
    "Priscila",
    "TOMAS",
    "Tomás",
    "Ulises",
    "Yanina","""
eva1 = """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74"""
eva2 = """30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
"""

#listas 
nombre = nombre.replace('"','').replace(',','').replace(' ','').split('\n')
eva1 = eva1.replace(',','').replace(' ','').split('\n')
eva2 = eva2.replace(',','').replace(' ','').split('\n')

def cargar_alumnos(i):
    """Retorna diccionario con los datos del alumno""" 
    dic = {}
    dic['nombre'] = nombre[i].capitalize()
    dic['nota 1'] = eva1[i]
    dic['nota 2'] = eva2[i]
    dic['nota final'] = int(eva1[i]) + int(eva2[i])
    return dic

def calc_prom_gral(lista_alu):
    "Retorna una cadena con la suma y el promedio de notas"
    suma = (sum(alum.get('nota final') for alum in lista_alu))
    promedio = suma / len(lista_alu)
    cad = f"Suma nota finales = {suma}  /  Promedio general = {round(promedio,2)}"
    return cad

def imprimir_listado(lista_alu):
    formato = "{:10} {:10} {:10} {:5}"  
    print(formato.format('Nombre','Nota 1','Nota 2','Nota final'))
    print(formato.format('------','------','------','--------'))
    for alu in lista_alu:
        print(formato.format(alu['nombre'],alu['nota 1'],alu['nota 2'],alu['nota final']))
    print(formato.format('------','------','------','--------'))

def menu_opciones(menu):
    while(menu != 0):
        menu =int(input("""
        ------------MENU--------------
        1 - Calcular promedio general
        2 - Generar reporte
        """))
        if(menu == 1):
            lista_dic = [cargar_alumnos(i) for i in range(len(nombre))]
            imprimir_listado(lista_dic)
            print(calc_prom_gral(lista_dic))

#invocaciones
menu_opciones(menu=-1)

