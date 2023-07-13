from database.conexion import DataBase
import hashlib

obj = DataBase()
herramienta = obj.conexion()

conexion = herramienta[0]
cursor = herramienta[1]

class Consultas():
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def crear_usuario(self):

        cifrar = hashlib.sha256()
        cifrar.update(self.password.encode('utf-8'))
        contraseña_hash = cifrar.hexdigest()
        
        sql = ("INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s,%s,%s,%s)")
        datos = (self.nombre, self.apellido, self.email, contraseña_hash)

        cursor.execute(sql, datos)
        conexion.commit()

        resultado = cursor.rowcount
        return resultado, self
    


    def logear_usuario(self):
        cifrar = hashlib.sha256()
        cifrar.update(self.password.encode('utf-8'))
        contraseña_decrypt = cifrar.hexdigest()
        

        sql = ("SELECT * FROM usuarios WHERE email = %s AND password = %s")
        datos= (self.email, contraseña_decrypt)

        cursor.execute(sql, datos)
        usuario = cursor.fetchone()

        resultado = cursor.rowcount
        return resultado, self, usuario
        