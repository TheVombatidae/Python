import Cads
import Func
import Listas         
   
def menu_opciones():
    menu = int(input(Cads.menu_principal))
    liberar = False
    while menu != 0:
        if menu == 1:
            lista_alu = [Func.cargar_alumnos(i) for i in range(len(Listas.nombre))]
            Func.imprimir_listado(lista_alu)
            print(Func.calc_prom_gral(lista_alu))
            liberar = True
        elif menu == 2 and liberar:
            submenu = input(Cads.submenu_a)
            if submenu.lower() == "d": pass
            elif(submenu.lower() == "a" or "b"):
                if submenu.lower() == "a":
                     nota="nota_1"
                else:
                     nota="nota_2"
                rango = Func.leer_rango(submenu)
                lista_n = list(filter(lambda dic: dic[nota] in rango ,lista_alu))
                Func.imprimir_listado(lista_n)
        if(not liberar):
            print(Cads.exc)
        menu = int(input(Cads.menu_principal))
    
#Global
exito = False
lista_alu = []
menu_opciones()
