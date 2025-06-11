import customtkinter as cus
import tkinter as tk
from tkinter import ttk as ttk
import tkcalendar as tkc

import sqlite3
from model import BaseDeDatos


class Estudiantes(cus.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.bd = BaseDeDatos()
        self.bd.crear_tabla_aluno()
        # bd.agregar_alumno()

        s = ttk.Style()
        s.theme_use("clam")
        s.configure("TreeView.Heading", background="lightblue", 
                    foreground="black", font=("Arial", 10, "bold"),
                    relief="raised")
        
        header_frame = cus.CTkFrame(self, height=70, fg_color="#5AB1FA")
        header_frame.place(x=0, y=0, relwidth=1, relheight=0.08)

        link_agregar = cus.CTkButton(header_frame, text="Agregar estudiantes", command=lambda:self.cambiar_vista("agregar"))
        link_lista = cus.CTkButton(header_frame, text="Lista", command=lambda:self.cambiar_vista("lista"))

        link_agregar.pack(side="right", padx=(5, 0))
        link_lista.pack(side="right")

        self.lista_de_cursos = ["1º Pep", "2º Pep", "3º Pep", "4º Pep",
            "5º Pep", "6º Pep", "1º Esba", "2º Esba",
            "3º Esba", "4º Esba", "1º Bach", "2º Bach"]

        self.lista_estudiantes()

    def lista_estudiantes(self):
        self.frm_lista = cus.CTkFrame(self, fg_color="#ffffff")
        self.frm_lista.place(x=0, y=0, relwidth=1, rely=0.09, relheight=1)

        # Ventana informativa de estudiantes
        frm_ventana = cus.CTkFrame(self.frm_lista, fg_color="#D6EBEE")
        frm_ventana.pack(anchor="nw", ipady=10)

        cus.CTkLabel(frm_ventana, text="160", font=("Arial", 30)).grid(row=0, column=0)
        cus.CTkLabel(frm_ventana, text="Estudiantes", font=("serif", 10)).grid(row=0, column=1, padx=(5, 100))

        cus.CTkLabel(frm_ventana, text="40", font=("Arial", 30)).grid(row=1, column=0)
        cus.CTkLabel(frm_ventana, text="Completos", font=("serif", 10)).grid(row=1, column=1, padx=(5, 100))

        cus.CTkLabel(frm_ventana, text="30", font=("Arial", 30)).grid(row=0, column=2)
        cus.CTkLabel(frm_ventana, text="Calendarios", font=("serif", 10)).grid(row=0, column=3, padx=(5, 100))

        cus.CTkLabel(frm_ventana, text="90", font=("Arial", 30)).grid(row=1, column=2)
        cus.CTkLabel(frm_ventana, text="Morosos", font=("serif", 10)).grid(row=1, column=3, padx=(5, 100))

        # Buscador de estudiantes
        frm_buscar = cus.CTkFrame(self.frm_lista, height=100)
        frm_buscar.pack(expand=True, fill="x", anchor="n", pady=5)
        frm_buscar.grid_propagate(False)
        frm_buscar.pack_propagate(False)

        buscador = cus.CTkEntry(frm_buscar, placeholder_text="       Buscar por Nombre o Apellido...", height=35)
        filt_curso = cus.CTkOptionMenu(frm_buscar, values=self.lista_de_cursos, height=35)
        filt_turno = cus.CTkOptionMenu(frm_buscar, values=["Mañana", "Tarde"], height=35)
        buscador.pack(side="left", expand=True, fill="x", padx=(50, 0))
        filt_curso.pack(side="left", padx=5)
        filt_turno.pack(side="left", padx=(0, 160))


        # Tabla de estudiantes
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
    
    def agregar_estudiantes(self):
        self.frm_agregar = cus.CTkFrame(self)
        self.frm_agregar.place(x=0, y=0, relwidth=1, rely=0.09, relheight=1)

        frm_info = cus.CTkFrame(self.frm_agregar)
        frm_info.pack(anchor="center", ipadx="10", ipady=5, padx=(0, 20))
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


        frm_formulario = cus.CTkFrame(self.frm_agregar, fg_color="#ffffff")
        frm_formulario.pack(pady=(20, 0))

        cus.CTkLabel(frm_formulario, text="Nombre", font=("Arial", 12), justify="left").grid(row=0, column=0, sticky="w", padx=10, pady=(20, 0))
        self.nombre_estudiante = cus.CTkEntry(frm_formulario, placeholder_text="  Aquí el nombre del estudiante...", width=200, height=35)
        self.nombre_estudiante.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0, 10))

        cus.CTkLabel(frm_formulario, text="Apellido", font=("Arial", 12), justify="left").grid(row=0, column=2, sticky="w", padx=10, pady=(20, 0))
        self.apellido_estudiante = cus.CTkEntry(frm_formulario, placeholder_text="  APELLIDO 1 APELLIDO 2...", width=200, height=35)
        self.apellido_estudiante.grid(row=1, column=2, padx=10, pady=(0, 10))

        cus.CTkLabel(frm_formulario, text="Curso", font=("Arial", 12), justify="left").grid(row=2, column=0, sticky="w", padx=10)
        self.curso = cus.CTkOptionMenu(frm_formulario, values=self.lista_de_cursos, height=35)
        self.curso.grid(row=3, column=0, padx=(10, 0), pady=10, sticky="nsew")

        cus.CTkLabel(frm_formulario, text="Fecha de nacimiento", font=("Arial", 12), justify="left").grid(row=2, column=1, sticky="w")
        self.fecha_nacimiento = tkc.DateEntry(frm_formulario, justify="center", width=20)
        self.fecha_nacimiento.grid(row=3, column=1, ipady=5, padx=10, pady=(0, 10))

        cus.CTkLabel(frm_formulario, text="Centro de procedencia", font=("Arial", 12), justify="left").grid(row=2, column=2, sticky="w", padx=10)
        self.centro_de_procedencia = cus.CTkEntry(frm_formulario, placeholder_text="  Centro de Ejemplo...", width=200, height=35)
        self.centro_de_procedencia.grid(row=3, column=2, padx=10, pady=(0, 10))

        cus.CTkLabel(frm_formulario, text="Tutor", font=("Arial", 12), justify="left").grid(row=4, column=0, sticky="w", padx=10)
        self.tutor = cus.CTkEntry(frm_formulario, placeholder_text="  Nombre del tutor...", width=200, height=35)
        self.tutor.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(0, 10), padx=10)

        cus.CTkLabel(frm_formulario, text="Dirección", font=("Arial", 12), justify="left").grid(row=4, column=2, sticky="w", padx=10)
        self.direccion = cus.CTkEntry(frm_formulario, placeholder_text="  Ntobo...", width=200, height=35)
        self.direccion.grid(row=5, column=2, padx=10, pady=(0, 10))

        cus.CTkLabel(frm_formulario, text="Teléfono", font=("Arial", 12), justify="left").grid(row=6, column=0, sticky="w", padx=10)
        self.tell = cus.CTkEntry(frm_formulario, placeholder_text="  (+240) 000 000 000", width=200, height=35)
        self.tell.grid(row=7, column=0, padx=10, pady=(0, 10))

        cus.CTkLabel(frm_formulario, text="Clase", font=("Arial", 12), justify="left").grid(row=6, column=1, sticky="w", padx=10)
        self.clase = cus.CTkOptionMenu(frm_formulario, values=["A", "B", "C"], width=50)
        self.clase.grid(row=7, column=1, padx=10, pady=(0, 10), sticky="w")

        self.turno = cus.CTkComboBox(frm_formulario, values=["Mañana", "Tarde"], justify="left")
        self.turno.grid(row=6, column=2, sticky="w", padx=10)

        self.var_calendario = tk.BooleanVar()
        self.calendario = cus.CTkCheckBox(frm_formulario, text="Calendario", variable=self.var_calendario)
        self.calendario.grid(row=7, column=2, padx=10, pady=(0, 10), sticky="w")

        self.btn_agregar = cus.CTkButton(frm_formulario, text="Agregar", command=self.validacion)
        self.btn_agregar.grid(row=8, column=0, columnspan=3, sticky="nsew", padx=10, pady=(50, 10))
    
    def validacion(self):
        self.check = self.var_calendario.get()
        if self.check:
            return self.toplevel_si_calendario()
        else:
            return self.toplevel_no_calendario()
    
    def toplevel_si_calendario(self):
        self.toplevel_cal = cus.CTkToplevel(self)
        self.toplevel_cal.geometry("400x250")
        self.toplevel_cal.grid_columnconfigure([0, 1], weight=1)
        self.toplevel_cal.attributes("-topmost", True)

        self.toplevel_cal.transient(self)
        self.toplevel_cal.grab_set()

        frm = cus.CTkFrame(self.toplevel_cal, fg_color="transparent")
        frm.grid(row=0, column=0, columnspan=2, sticky="nsew")
        frm.grid_columnconfigure([0, 1], weight=1)
        frm.grid_propagate(False)

        frm_2 = cus.CTkFrame(self.toplevel_cal, fg_color="grey32")
        frm_2.grid_columnconfigure([0, 1], weight=1)
        frm_2.grid_propagate(False)
        frm_2.grid(row=1, column=0, columnspan=2, sticky="nsew")

        cus.CTkLabel(frm, text="Nombre del calendario").grid(row=0, column=0, columnspan=2, sticky="nsew", padx=30, pady=(30, 0))
        self.nom_calendario = cus.CTkComboBox(frm, height=30, justify="center")
        self.nom_calendario.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=30)

        cus.CTkLabel(frm, text="Ingreso").grid(row=2, column=0, columnspan=2, sticky="nsew", padx=30)
        self.ingreso = cus.CTkEntry(frm, placeholder_text=" 80.000 Fcf", justify="center", width=100, height=30)
        self.ingreso.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=30)

        self.btn_calendario = cus.CTkButton(frm_2, text="Aceptar", command=self.validar_datos_calendario)
        self.btn_calendario.grid(row=0, column=1, sticky="e", padx=30, pady=(10, 0))
    
    def toplevel_no_calendario(self):
        self.toplevel_no = cus.CTkToplevel(self)
        self.toplevel_no.geometry("400x250")
        self.toplevel_no.grid_columnconfigure([0, 1], weight=1)
        self.toplevel_no.attributes("-topmost", True)

        self.toplevel_no.transient(self)
        self.toplevel_no.grab_set()

        frm = cus.CTkFrame(self.toplevel_no, fg_color="transparent")
        frm.grid(row=0, column=0, columnspan=2, sticky="nsew")
        frm.grid_columnconfigure([0, 1], weight=1)
        frm.grid_propagate(False)

        frm_2 = cus.CTkFrame(self.toplevel_no, fg_color="grey32")
        frm_2.grid_columnconfigure([0, 1], weight=1)
        frm_2.grid_propagate(False)
        frm_2.grid(row=1, column=0, columnspan=2, sticky="nsew")

        cus.CTkLabel(frm, text="Ingreso").grid(row=0, column=0, columnspan=2, sticky="nsew", padx=30, pady=(30, 0))
        self.matricula = cus.CTkEntry(frm, placeholder_text=" 80.000 Fcf", justify="center", width=100, height=30)
        self.matricula.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=30)

        self.btn_calendario_no = cus.CTkButton(frm_2, text="Aceptar", command= self.validar_datos_no)
        self.btn_calendario_no.grid(row=0, column=1, sticky="e", padx=30, pady=(10, 0))



    
    def destroy_toplevel(self):
        # self.toplevel_cal.destroy()
        self.toplevel_no.destroy()
    
    def validar_datos_no(self):
        nombre = self.nombre_estudiante.get()
        apellido = self.apellido_estudiante.get()
        curso = self.curso.get()
        clase = self.clase.get()
        turno = self.turno.get()
        centro = self.centro_de_procedencia.get()
        tutor = self.tutor.get()
        tell = self.tell.get()
        direccion = self.direccion.get()
        calendario = self.calendario.get()
        matricula = int(self.matricula.get())
        fecha = self.fecha_nacimiento.get_date()

        self.bd.agregar_alumno(nombre, apellido, curso, clase, turno, centro, tutor, tell, direccion, calendario, matricula, fecha)

    
    def validar_datos_calendario(self):
        nombre = self.nombre_estudiante.get()
        apellido = self.apellido_estudiante.get()
        curso = self.curso.get()
        clase = self.clase.get()
        turno = self.turno.get()
        centro = self.centro_de_procedencia.get()
        tutor = self.tutor.get()
        tell = self.tell.get()
        direccion = self.direccion.get()
        calendario = self.nom_calendario.get()
        matricula = int(self.ingreso.get())
        fecha = self.fecha_nacimiento.get_date()

        self.bd.agregar_alumno(nombre, apellido, curso, clase, turno, centro, tutor, tell, direccion, calendario, matricula, fecha)

        

    
    def cambiar_vista(self, vista):
        if vista == "agregar":
            if hasattr(self, 'frm_lista'):
                self.frm_lista.destroy()
                self.agregar_estudiantes()
        else:
            if hasattr(self, 'frm_agregar'):
                self.frm_agregar.destroy()
                self.lista_estudiantes()