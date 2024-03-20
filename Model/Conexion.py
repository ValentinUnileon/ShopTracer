import mysql.connector


class Conexion:


    def __init__(self):

        pass

    def getDatabaseConexion(self):

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            #password is not needed
            database="shoptracedatabase"
        )
        
        # Crear un cursor
        #mycursor = mydb.cursor()

        print("Conexión exitosa!")

        return mydb

        


        # Ejecutar una consulta SQL
        #self.mycursor.execute("SELECT * FROM shop")

        # Obtener los resultados
        #resultados = self.mycursor.fetchall()

        # Imprimir los resultados
        #for fila in resultados:
        #    print(fila)
