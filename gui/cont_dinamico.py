import customtkinter as cus
import tkinter as tk


class Main(cus.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        cus.CTkLabel(self, text="Main", anchor="center").pack(expand=True, fill="both")

        self.place(relx=0.122, y=0, relwidth=0.87, relheight=1)
    
    def limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    # Motrar el contenido de la clase según el botón seleccionado
    def cambiar_contenido(self, clase):
        self.limpiar()
        vista = clase(self)
        vista.pack(fill="both", expand=True)