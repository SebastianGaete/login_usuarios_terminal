from .consultasqls import Consultas

class Usuario():
    
    def registrarse(self):
        nombre = input('Ingrese su nombre >> ')
        apellido = input('Ingrese su apellido >> ')
        email = input('Ingrese su email >> ')
        password = input('Ingrese su contraseña >> ')

        usuario = Consultas(nombre, apellido, email, password)
        usuario_creado = usuario.crear_usuario()

        if usuario_creado[0] >= 1:
            print(f'Bienvenido {nombre} te has registrado correctamente!')
        else:
            print('No te has registrado correctamente!')


    def ingresar(self):
        email = input('Ingrese su email >> ')
        password = input('Ingrese su contraseña >> ')

        usuario = Consultas('', '', email, password)
        usuario_logeado = usuario.logear_usuario()

        if usuario_logeado[0] >= 1:
            print(f'Te estabamos extrañando {usuario_logeado[2][1]} {usuario_logeado[2][2]} gracias por volver! ')
        else:
            print('No hay ningún usuario registrado con estas credenciales!')



    
