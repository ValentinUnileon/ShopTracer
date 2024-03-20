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
            for row in resultados:
                print(row)
                
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta SQL:", err)

