import customtkinter as cus
import tkinter as tk
import sqlite3
from modules.students import Students
from modules.subjects import Subjects

class GesApp(cus.CTk):
    def __init__(self, title):
        super().__init__()

        self.minsize(width=900, height=500)
        self.title(title)

        cus.set_appearance_mode("light")

        # Clases principales
        self.menu = Menu(self, self.mostrar_seccion)
        self.main = Main(self)

        # Diccionario de secciones
        self.secciones = {
            "Inicio": self.mostrar_inicio,
            "Estudiantes": lambda:self.main.cambiar_contenido(Students),
            # "profesores": lambda:self.main_cambiar_contenido(Profesores),
            "Asignaturas": lambda:self.main.cambiar_contenido(Subjects),
        }

        self.mostrar_inicio()
    def mostrar_seccion(self, nombre):
        if nombre in self.secciones:
            self.secciones[nombre]() # Ejecuta la funciçon mostrar_inicio

    def mostrar_inicio(self):
        self.main.limpiar()
        label = cus.CTkLabel(self.main, text="Bienvenido a GES", font=("Arial", 24))
        label.pack(pady=40, expand=True, anchor="center")


class Menu(cus.CTkFrame):
    def __init__(self, master, callback, **kwargs):
        super().__init__(master, fg_color="#111827", **kwargs)
        self.callback = callback
        self.pack(side="left", fill="y")
        botones = ["Inicio", "Estudiantes", "Profesores", "Asignaturas"]
        for texto in botones:
            btn = cus.CTkButton(self, text=texto, command=lambda t=texto:self.callback(t))
            btn.pack(pady=10, padx=10, fill="x")


class Main(cus.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side="right", fill="both", expand=True)

    def limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def cambiar_contenido(self, clase):
        self.limpiar()
        vista = clase(self)
        vista.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = GesApp("GES")
    app.mainloop()
