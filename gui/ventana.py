import customtkinter as cus
import tkinter as tk

from gui.menu import Menu
from gui.secciones.panel_control import Panel
from gui.secciones.estudiantes import Estudiantes
from gui.secciones.profesores import Profesores
from gui.secciones.asignaturas import Asignaturas
from gui.cont_dinamico import Main

from model import BaseDeDatos

from .menu import Menu


class App(cus.CTk):
    def __init__(self,title, fg_color = "gray15", **kwargs):
        super().__init__(fg_color, **kwargs)

        bd_a = BaseDeDatos()
        bd_a.crear_tabla_aluno()

        self.geometry("800x600")
        self.title(title)

        cus.set_appearance_mode("light")

        self.main = Main(self)
        self.menu = Menu(self, self.mostrar_seccion)

        self.secciones = {
            "Panel": self.mostrar_inicio,
            "Estudiantes": lambda:self.main.cambiar_contenido(Estudiantes),
            "Profesores": lambda:self.main.cambiar_contenido(Profesores),
            "Asignaturas": lambda:self.main.cambiar_contenido(Asignaturas),
            # "AMPA": lambda:self.main.cambiar_contenido(AMPA),
            # "Boletin": lambda:self.main.cambiar_contenido(Boletin)
        }

        self.mostrar_inicio()

    def mostrar_inicio(self):
        self.main.limpiar()
        self.panel = Panel(self.main)
        self.panel.pack(expand=True, fill="both")
    
    def mostrar_seccion(self, nombre):
        if nombre in self.secciones:
            self.secciones[nombre]()

# if __name__=="__main__":
#     app = App("GES")
#     app.mainloop()