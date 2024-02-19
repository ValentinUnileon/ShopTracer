import customtkinter as ctk

class PrincipalView:

    def __init__(self):
        self.runAppInterface()  # Debe ser llamado como un método de instancia

    def runAppInterface(self):  # Agregar self como primer argumento

        #Creacion de la pantalla principal
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        app = ctk.CTk()  # create CTk window like you do with the Tk window
        app.geometry("1420x650")


        def button_function():
            print("button pressed")


        # Crear el primer frame (columna izquierda)
        left_column = ctk.CTkFrame(app, width=350)
        left_column.pack(side="left", fill="y", padx=0, pady=0)  # Columna izquierda ocupa toda la altura

        #Frame de categorias a la derecha
        categoriesFrame = ctk.CTkFrame(app, width=370 ,fg_color="green")
        categoriesFrame.pack(side="right", fill="y", padx=0, pady=0)

        # Crear el segundo frame (frame para mostrar la imagen del plano)
        planeFrame = ctk.CTkFrame(app, height=400, width=900, fg_color="black")
        planeFrame.pack(anchor='nw', padx=0, pady=0)  # Relativo al ancho y alto de la ventana nw = north west

        #Tercer frame debajo del plano

        shopFrame = ctk.CTkFrame(app, height=250, width=900, fg_color="blue")
        shopFrame.pack(anchor = 'sw', padx=0, pady=0)

        #Frame de categorias a la izquierda



        # El valor de relx indica la posición en el eje x relativa al ancho total de la ventana.
        # El valor de relwidth indica el ancho relativo al ancho total de la ventana.
        # El valor de relheight indica la altura relativa al alto total de la ventana.

        #Boton dentro del frame

        button = ctk.CTkButton(master=left_column, text="CTkButton", command=button_function)
        button.place(relx=0.1, rely=0.5, anchor=ctk.W)  # Coloca el botón a la izquierda

        #Campo de texto dentro del frame

        textbox = ctk.CTkTextbox(master=left_column, width=200, corner_radius=0, fg_color="transparent")
        textbox.grid(row=0, column=0, sticky="nsew")
        textbox.insert("0.0", "Some example text!\n")

        app.mainloop()
