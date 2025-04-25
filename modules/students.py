import customtkinter as cus
import tkinter as tk
from tkinter import ttk
import sqlite3

class Students(cus.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.conectar_db()
        self.create_Widgets()
        self.cargar_estudiamtes()
    
    def conectar_db(self):
        conn = sqlite3.connect("ges.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    apellido TEXT,
                    fecha_nacimiento TEXT,
                    procedencia TEXT,
                    tutor1 TEXT,
                    tutor2 TEXT,
                    telefono TEXT,
                    direccion TEXT)""")
        conn.commit()
        # conn.close()
    
    def cargar_estudiamtes(self):
        # Limpiar la tabla antes de cargar
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
        conn = sqlite3.connect("ges.db")
        cursor = conn.cursor()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, apellido procedencia FROM estudiantes")
        estudiantes = cursor.fetchall()
        conn.close()

        for estudiante in estudiantes:
            self.tabla.insert("", "end", values=estudiante)

    
    def create_Widgets(self):
        tabs = ttk.Notebook(self)
        self.tab_search = cus.CTkFrame(tabs)
        self.tab_add = cus.CTkFrame(tabs)

        tabs.add(self.tab_search, text="Buscar")
        tabs.add(self.tab_add, text="Agregar")

        tabs.pack(fill="both", expand=True, padx=20, pady=10)

        # TAB Buscar estudiantes
        self.entry_buscar = cus.CTkEntry(self.tab_search, placeholder_text="Buscar por nombre o apellido")
        self.entry_buscar.pack(fill="x", padx=20, pady=10)
        self.entry_buscar.bind("<KeyRelease>", self.buscar_estudiantes)

        self.tabla = ttk.Treeview(self.tab_search, columns=("Nombre", "Apellido", "Curso"), show="headings")

        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Curso", text="Curso")

        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

        # TAB Agregar estudiantes
        cont = cus.CTkFrame(self.tab_add)
        cont.pack(side="left", anchor="center", expand=True, padx=(50, 0))

        self.entry_name = cus.CTkEntry(cont, placeholder_text="Nombre del estudiante", width=300, height=35)
        self.entry_apellido = cus.CTkEntry(cont, placeholder_text="Apellido", width=250, height=35)
        self.entry_fecha = cus.CTkEntry(cont, placeholder_text="Fecha de nacimiento", width=250, height=35)
        self.entry_procedencia = cus.CTkEntry(cont, placeholder_text="Centro de procedencia", width=300, height=35)
        self.entry_tutor1 = cus.CTkEntry(cont, placeholder_text="Nombre del tutor 1", width=250, height=35)
        self.entry_tutor2 = cus.CTkEntry(cont, placeholder_text="Tutor 2", width=250, height=35)
        self.entry_tell = cus.CTkEntry(cont, placeholder_text="Tell: +240 *** *** ***", width=300, height=35)
        self.entry_direccion = cus.CTkEntry(cont, placeholder_text="Direción", width=250, height=35)

        self.entry_name.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=(40, 10))
        self.entry_apellido.grid(row=0, column=2, sticky="nsew", padx=5, pady=(40, 10))
        self.entry_fecha.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)
        self.entry_procedencia.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)
        self.entry_tutor1.grid(row=2, column=0, sticky="nsew", padx=5, pady=10)
        self.entry_tutor2.grid(row=2, column=2, sticky="nsew", padx=5, pady=10)
        self.entry_tell.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
        self.entry_direccion.grid(row=3, column=2, sticky="nsew", padx=5, pady=10)

        self.add_student = cus.CTkButton(cont, text="Agregar estudiante", command=self.agregar_estudiantes)
        self.add_student.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=(40, 20), padx=80)
    
    def agregar_estudiantes(self):
        datos =(
            self.entry_name.get(),
            self.entry_apellido.get(),
            self.entry_fecha.get(),
            self.entry_procedencia.get(),
            self.entry_tutor1.get(),
            self.entry_tutor2.get(),
            self.entry_tell.get(),
            self.entry_direccion.get()
        )

        conn = sqlite3.connect("ges.db")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO estudiantes(
                       nombre, apellido, fecha_nacimiento,
                       procedencia, tutor1, tutor2,
                       telefono, direccion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", datos)
        conn.commit()
        conn.close()

        self.limpiar_campos()
        self.cargar_estudiamtes()

    def buscar_estudiantes(self, event=None):
        termino = self.entry_buscar.get().lower()

        conn = sqlite3.connect("ges.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, apellido, procedencia FROM estudiantes")
        estudiantes = cursor.fetchall()
        conn.close()

        self.tabla.delete(*self.tabla.get_children())

        for est in estudiantes:
            nombre, apellido, procedencia = est
            if termino in nombre.lower() or termino in apellido.lower():
                self.tabla.insert("", "end", values=(nombre, apellido, procedencia))

    def limpiar_campos(self):
        for entry in [self.entry_name, self.entry_apellido, self.entry_fecha,
                      self.entry_procedencia, self.entry_tutor1, self.entry_tutor2,
                      self.entry_tell, self.entry_direccion
                      ]:
            entry.delete(0, "end")

# if __name__ == "__main__":
#     root = cus.CTk()
#     root.title("GES")
#     root.geometry("900x500")
#     app = Students(master=root)
#     root.mainloop()
