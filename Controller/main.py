import sys
sys.path.append('../View')  # Agregar la carpeta 'View' al PYTHONPATH

from principalView import PrincipalView  # Importar la clase PrincipalView desde principal_view.py

if __name__ == "__main__":
    principal_view = PrincipalView()  # Crear una instancia de la clase PrincipalView -- se ejecuta la funcion desplegar interfaz porque en el constructor de view se llama 
