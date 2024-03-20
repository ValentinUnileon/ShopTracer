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

    def setFloorObject(self, floorVO):

        #first check if the object is in the database to be able to delete it 
        


