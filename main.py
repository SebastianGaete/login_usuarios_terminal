import usuarios.peticiones as peticiones
realiza = peticiones.Usuario()

def inicio():
    print("""
    =========================
            Bienvenido   
     ========================= 
          
    [1] Registrarse
    [2] Ingresar
    [3] Salir
    
    """)
    opcion = int(input('Selecciona una opción >> '))

    match opcion:
        case 1:
            realiza.registrarse()
            """
            Si se ingresa la opcion 1 debo preguntar al usuario que ingrese sus datos ya indicados en la BBDD que cree, pero para no hacerlo tan largo
            esas peticiones las haré en otro fichero utilizando una clase. para despues invocarla por este medio a travez de una instancia de ella.
            """
        case 2:
            realiza.ingresar()
        case 3:
            print('Gracias por tu preferencia!')
            exit()
        case _:
            print('Ingrese una opción valida!')



if __name__ == '__main__':
    inicio()

    