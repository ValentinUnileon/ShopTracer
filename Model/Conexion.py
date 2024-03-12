import mysql.connector


class Conexion:

    def __init__(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="shoptracedatabase"
        )

        print("Conexión exitosa!")

        # Crear un cursor
        mycursor = mydb.cursor()

        # Ejecutar una consulta SQL
        mycursor.execute("SELECT * FROM category")

        # Obtener los resultados
        resultados = mycursor.fetchall()

        # Imprimir los resultados
        for fila in resultados:
            print(fila)
