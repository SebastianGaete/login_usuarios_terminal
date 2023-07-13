import database.conexion as db
import bcrypt

DB = db.DataBase()
DDBB = DB.conexion()

conexion = DDBB[0]
cursor = DDBB[1]

class Consultas():
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def crear_usuario(self):
        
        sql = ("INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s,%s,%s,%s)")
        datos = (self.nombre, self.apellido, self.email, self.password)

        cursor.execute(sql, datos)
        conexion.commit()

        resultado = cursor.rowcount
        return resultado, self
    


    def logear_usuario(self):

        sql = ("SELECT * FROM usuarios WHERE email = %s AND password = %s")
        datos= (self.email, self.password)

        cursor.execute(sql, datos)
        usuario = cursor.fetchone()

        resultado = cursor.rowcount
        return resultado, self, usuario
        
