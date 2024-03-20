import sys
sys.path.append('../View')  # Agregar la carpeta 'View' al PYTHONPATH
sys.path.append('../Model')


from PrincipalView import PrincipalView 
from ViewController import ViewController
from Conexion import Conexion
from DAO.FloorDAO import FloorDAO


if __name__ == "__main__":
    
    # Crear una instancia de la clase PrincipalView -- se ejecuta la funcion desplegar interfaz porque en el constructor de view se llama 
    controller = ViewController()
    conexion = Conexion()

    
    floorDAO= FloorDAO()

    floor= floorDAO.getFloorObject(1)

    print("mira  ", floor.getFloorImage())


    principal_view = PrincipalView(controller)  
    controller.setView(principal_view)



    #ahora seteamos la vista en el controlador 

