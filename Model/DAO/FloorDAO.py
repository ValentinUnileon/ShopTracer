import sys
sys.path.append('../Model') 

import mysql

from VO.FloorVO import FloorVO
from Conexion import Conexion


class FloorDAO:

    def __init__(self):
        pass

    def getFloorObject(self, idFloor):

        floor= FloorVO()
        conexion = Conexion()
        mydb = conexion.getDatabaseConexion()
  

        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM floor WHERE floor_id=%s", (idFloor,))
            resultados = cursor.fetchall()


            floor.setFloorID(resultados[0][0])
            floor.setFloorNumber(resultados[0][1])
            floor.setFloorImage(resultados[0][2])

        except mysql.connector.Error as err:

            #Check if the object is in the database
            print("Error", err)

        return floor

    def createFloorObject(self, floorVO):

        #First check if the object is in the database to be able to delete it 

        conexion = Conexion()
        mydb = conexion.getDatabaseConexion()
        cursor = mydb.cursor()

        try:
            cursor.execute("SELECT COUNT(*) FROM floor WHERE floor_id = %s", (floorVO.getFloorID(),))
            resultado = cursor.fetchone()[0]

        except mysql.connector.Error as err:

            print("Error", err)

        # Check if the object is in the database
        if resultado == 1:

            print("El objeto está en la base de datos.")
            #Then we CANT create it


        else:
            print("El objeto no está en la base de datos.")
            #Then we create it

            # Query para insertar el objeto en la base de datos
            query_insert = "INSERT INTO floor (floor_id, number, image) VALUES (%s, %s, %s)"

            # Valores a insertar
            valores = (floorVO.getFloorID(), floorVO.getFloorNumber(), floorVO.getFloorImage())

            # Ejecutar la consulta SQL para insertar el objeto en la base de datos
            cursor.execute(query_insert, valores)

            # Confirmar la operación de inserción
            mydb.commit()

            # Informar al usuario que el objeto ha sido creado exitosamente
            print("El objeto ha sido creado exitosamente en la base de datos.")




