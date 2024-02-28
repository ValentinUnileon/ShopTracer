import sys
sys.path.append('../View')  # Agregar la carpeta 'View' al PYTHONPATH

import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image

from PrincipalView import PrincipalView 

class ViewController:

    def __init__(self):
        print("afsd")
        self.principal_view = None  # Corrección del nombre del atributo
    
    def setView(self, view):
        self.principal_view = view  # Corrección del nombre del atributo

    def press(self, label):
        print("FUNCIONA")

        image = PhotoImage(file="../Images/estacion-de-carga.png")
        #print(self.principal_view)
        plan = ctk.CTkImage(light_image=Image.open("../Images/estacion-de-carga.png"), size=(850, 400))
        label.configure(image=plan)
        label.pack(padx=0, pady=0)

