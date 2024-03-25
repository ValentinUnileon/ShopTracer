import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image
import time

class PrincipalView:

    buttonIcon = None  
    label_hora = None
    app= None
     #CONSTRUCTOR de la clase - se le pasa como argumento el controlador

    def __init__(self, viewController): 
        self.viewController = viewController
        self.image_label = None
        self.left_column = None
        self.planeFrame = None

        self.runAppInterface()  # Debe ser llamado como un método de instancia

    def controllerData(self):
        return self.viewController.getNum()
    
    def update_hour(self):
        hora_actual = time.strftime('%H:%M:%S')
        self.label_hora.configure(text=hora_actual)
        self.app.after(1000, self.update_hour)
    
    def runAppInterface(self):  # Agregar self como primer argumento

        #Creacion de la pantalla principal
        ctk.set_appearance_mode("System")           # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")         # Themes: blue (default), dark-blue, green
        self.app = ctk.CTk()                             # create CTk window like you do with the Tk window
        self.app.geometry("1420x650")


        def button_function():
            print("button pressed")


        # Crear el primer frame (columna izquierda)
            
        left_column = ctk.CTkFrame(self.app, width=350)
        left_column.pack(side="left", fill="y", padx=0, pady=0)     # Columna izquierda ocupa toda la altura


            #Boton dentro del frame

        button = ctk.CTkButton(master=left_column, text="CTkButton", command=button_function)
        button.place(relx=0.1, rely=0.5, anchor=ctk.W)  # Coloca el botón a la izquierda


            #Campo de texto dentro del frame

        #textbox = ctk.CTkTextbox(master=left_column, width=200, corner_radius=0, fg_color="transparent")
        #textbox.grid(row=0, column=0, sticky="nsew")
        #textbox.insert("0.0", "Some example text!\n")

        self.label_hora = ctk.CTkLabel(left_column, font=('Roboto', 48), fg_color='transparent')
        self.label_hora.grid(row=0, column=0, padx=10, pady=10)
        self.label_hora.configure(text="Nuevo texto")

        self.update_hour()


        #Frame de categorias a la derecha


        categoriesFrame = ctk.CTkFrame(self.app, width=370 ,fg_color="transparent")
        categoriesFrame.pack(side="right", fill="y", padx=0, pady=0)

        entry = ctk.CTkEntry(master=categoriesFrame,width=370, placeholder_text="Introduce something")
        entry.pack(side="top", fill="x", padx=0, pady=20)


        # Crear el segundo frame (frame para mostrar la imagen del plano)


        planeFrame = ctk.CTkFrame(self.app, height=400, width=900, fg_color="transparent")
        planeFrame.pack(anchor='nw', padx=0, pady=0)  # Relativo al ancho y alto de la ventana nw = north west padx y pady separaciones

            #se establece la imagen del plano

        plan = ctk.CTkImage(light_image=Image.open("../Images/pngwing.com.png"), size=(850, 400))

        self.image_label = ctk.CTkLabel(planeFrame, image=plan, text="")     # display image with a CTkLabel

        self.image_label.pack(padx=0, pady=0)


        #Tercer frame debajo del plano

        shopFrame = ctk.CTkFrame(self.app, height=250, width=900, fg_color="transparent")
        shopFrame.pack(anchor = 'sw', padx=0, pady=0)


        image = PhotoImage(file="../Images/estacion-de-carga.png")
        image = image.subsample(5)                                      # Redimensionar la imagen a la mitad

        self.buttonIcon = ctk.CTkButton(master=shopFrame, text="", command=lambda: self.viewController.press(self.image_label), image=image, fg_color="transparent", width=80, height=80)
        
        #establecemos el side a left para que los botones se distribullan horizontalmente
        
        self.buttonIcon.pack(side="left", padx=5, pady=5) 

        imageToilet = PhotoImage(file="../Images/macho-femenino.png")
        imageToilet = imageToilet.subsample(5)  # Redimensionar la imagen a la mitad

        buttonIcon2 = ctk.CTkButton(master=shopFrame, text="", command=lambda: self.viewController.press(self.image_label), image=imageToilet, fg_color="transparent", width=80, height=80)
        buttonIcon2.pack(side="left", padx=5, pady=5)
        

        #Frame de categorias a la izquierda

        # El valor de relx indica la posición en el eje x relativa al ancho total de la ventana.
        # El valor de relwidth indica el ancho relativo al ancho total de la ventana.
        # El valor de relheight indica la altura relativa al alto total de la ventana.


        self.app.mainloop()

      

 



