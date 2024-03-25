import sys
sys.path.append('../View')  # Agregar la carpeta 'View' al PYTHONPATH

import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image

from PrincipalView import PrincipalView 

class ViewController:

    def __init__(self):
        self.principal_view = None  # Corrección del nombre del atributo
    
    def setView(self, view):
        self.principal_view = view  # Corrección del nombre del atributo

    def press(self, label):
        print("FUNCIONA")

        #print(self.principal_view)
        plan = ctk.CTkImage(light_image=Image.open("../Images/planModified.png"), size=(850, 400))
        label.configure(image=plan)
        label.pack(padx=0, pady=0)

