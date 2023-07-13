import psycopg2

class DataBase():

    def conexion(self):
        self.conexion = psycopg2.connect(
            database='db_appnotas',
            host='localhost',
            port='',
            user='postgres',
            password='warcrychile123'
        )

        self.cursor = self.conexion.cursor()
        
        return [self.conexion, self.cursor]
    
