import customtkinter as cus
import tkinter as tk
from tkinter import ttk as ttk
import tkcalendar as tkc

import sqlite3

class Profesores(cus.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        # bd.agregar_alumno()

        s = ttk.Style()
        s.theme_use("clam")
        s.configure("TreeView.Heading", background="lightblue", 
                    foreground="black", font=("Arial", 10, "bold"),
                    relief="raised")
        
        header_frame = cus.CTkFrame(self, height=70, fg_color="#5AB1FA")
        header_frame.place(x=0, y=0, relwidth=1, relheight=0.08)

        link_agregar = cus.CTkButton(header_frame, text="Agregar profesores", command=lambda:self.cambiar_vista("agregar"))
        link_lista = cus.CTkButton(header_frame, text="Lista", command=lambda:self.cambiar_vista("lista"))

        link_agregar.pack(side="right", padx=(5, 0))
        link_lista.pack(side="right")

        self.lista_de_cursos = ["1º Pep", "2º Pep", "3º Pep", "4º Pep",
            "5º Pep", "6º Pep", "1º Esba", "2º Esba",
            "3º Esba", "4º Esba", "1º Bach", "2º Bach"]

        self.lista_profesores()

    def lista_profesores(self):
        self.frm_lista = cus.CTkFrame(self, fg_color="#ffffff")
        self.frm_lista.place(x=0, y=0, relwidth=1, rely=0.09, relheight=1)

        # Ventana informativa de profesores
        frm_ventana = cus.CTkFrame(self.frm_lista, fg_color="#D6EBEE")
        frm_ventana.pack(anchor="ne", ipady=10)

        cus.CTkLabel(frm_ventana, text="160", font=("Arial", 30)).grid(row=0, column=0)
        cus.CTkLabel(frm_ventana, text="profesores", font=("serif", 10)).grid(row=0, column=1, padx=(5, 100))

        cus.CTkLabel(frm_ventana, text="40", font=("Arial", 30)).grid(row=1, column=0)
        cus.CTkLabel(frm_ventana, text="Completos", font=("serif", 10)).grid(row=1, column=1, padx=(5, 100))

        cus.CTkLabel(frm_ventana, text="30", font=("Arial", 30)).grid(row=0, column=2)
        cus.CTkLabel(frm_ventana, text="Calendarios", font=("serif", 10)).grid(row=0, column=3, padx=(5, 100))

        cus.CTkLabel(frm_ventana, text="90", font=("Arial", 30)).grid(row=1, column=2)
        cus.CTkLabel(frm_ventana, text="Morosos", font=("serif", 10)).grid(row=1, column=3, padx=(5, 100))

        # Buscador de profesores
        frm_buscar = cus.CTkFrame(self.frm_lista, height=100)
        frm_buscar.pack(expand=True, fill="x", anchor="n", pady=5)
        frm_buscar.grid_propagate(False)
        frm_buscar.pack_propagate(False)

        buscador = cus.CTkEntry(frm_buscar, placeholder_text="       Buscar por Nombre o Apellido...", height=35)
        btn_buscar = cus.CTkButton(frm_buscar, text="Buscar", height=35, width=150)
        buscador.pack(side="left", expand=True, fill="x", padx=(50, 0))
        btn_buscar.pack(side="left", padx=(5, 200))


        # Tabla de Profesores
        frm_tabla = cus.CTkFrame(self.frm_lista)
        frm_tabla.pack(expand=True, fill="both")

        tabla = ttk.Treeview(frm_tabla, columns=("col1", "col2", "col3", "col4", "col5"), show="headings", height=300)

        tabla.heading("col1", text="Nombre")
        tabla.heading("col2", text="Apellido")
        tabla.heading("col3", text="Curso")
        tabla.heading("col4", text="Clase")
        tabla.heading("col5", text="Turno")

        tabla.column("col1", width=150, anchor="w", stretch=True)
        tabla.column("col2", width=150, anchor="w")
        tabla.column("col3", width=150, anchor="w")
        tabla.column("col4", width=150, anchor="w")
        tabla.column("col5", width=150, anchor="w")

        tabla.pack(expand=True, fill="both")
    
    def agregar_profesores(self):
        self.frm_agregar = cus.CTkFrame(self)
        self.frm_agregar.place(x=0, y=0, relwidth=1, rely=0.09, relheight=1)

        frm_info = cus.CTkFrame(self.frm_agregar)
        frm_info.pack(anchor="e", ipadx="10", ipady=5, padx=(0, 20))
        cus.CTkLabel(frm_info, text="Del cuso seleccionado quedan", font=("Arial", 20, "bold"), justify="left").grid(row=0, column=0, columnspan=4, sticky="w")
        cus.CTkLabel(frm_info, text="Mañana", font=("Arial", 16, "bold"), justify="left").grid(row=1, column=0, columnspan=2, sticky="w")
        cus.CTkLabel(frm_info, text="Clase A:", font=("Arial", 10, "bold"), justify="left").grid(row=2, column=0, sticky="w")
        cus.CTkLabel(frm_info, text="27", font=("sans", 16, "bold"), justify="left").grid(row=2, column=1, sticky="w")
        cus.CTkLabel(frm_info, text="Clase B:", font=("Arial", 10, "bold"), justify="left").grid(row=3, column=0, sticky="w")
        cus.CTkLabel(frm_info, text="21", font=("sans", 16, "bold"), justify="left").grid(row=3, column=1, sticky="w")

        cus.CTkLabel(frm_info, text="Tarde", font=("Arial", 16, "bold"), justify="left").grid(row=1, column=2, columnspan=2, sticky="w")
        cus.CTkLabel(frm_info, text="Clase A:", font=("Arial", 10, "bold"), justify="left").grid(row=2, column=2, sticky="w")
        cus.CTkLabel(frm_info, text="27", font=("sans", 16, "bold"), justify="left").grid(row=2, column=3, sticky="w")
        cus.CTkLabel(frm_info, text="Clase B:", font=("Arial", 10, "bold"), justify="left").grid(row=3, column=2, sticky="w")
        cus.CTkLabel(frm_info, text="21", font=("sans", 16, "bold"), justify="left").grid(row=3, column=3, sticky="w")


        frm_formulario = cus.CTkFrame(self.frm_agregar)
        frm_formulario.pack(pady=(20, 0))

    def cambiar_vista(self, vista):
        if vista == "agregar":
            if hasattr(self, 'frm_lista'):
                self.frm_lista.destroy()
                self.agregar_profesores()
        else:
            if hasattr(self, 'frm_agregar'):
                self.frm_agregar.destroy()
                self.lista_profesores()