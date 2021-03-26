Cad = input("Ingrese una clave(maximo 10 caracteres) \nCaracteres Prohibidos: ! y @ \nPassword: ")

if ('!' in Cad or '@' in Cad or len(Cad) > 10):
        print('Error superaste los diez caracteres o ingresaste un caracter prohibido')
else:
    print('Ingreso correcto')
            
