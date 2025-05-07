import customtkinter as cus
from tkinter import ttk
import sqlite3

class Subjects(cus.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=20, pady=20, fill="both", expand=True)

        # Titulo
        self.label = cus.CTkLabel(self, text="Asignaturas", font=("Arial", 24))
        self.label.pack(pady=(10, 20))

        # Selección de grado
        self.grado_combo = cus.CTkComboBox(self, values=[
            "1º Primaria", "2º Primaria", "3º Primaria", "4º Primaria",
            "5º Primaria", "6º Primaria", "1º Eso", "2º Eso", "3º Eso",
            "4º Eso", "1º Bachillerato", "2º Bachillerato"
        ])
        self.grado_combo.set("1º Primaria")
        self.grado_combo.pack(fill="x", pady=(0, 10))

        # Lista de asignaturas (Treeview)
        self.lista_asignaturas = ttk.Treeview(self, columns=("Grado", "Asignatura"), show="headings")
        self.lista_asignaturas.heading("Grado", text="Grado")
        self.lista_asignaturas.heading("Asignatura", text="Asignatura")
        self.lista_asignaturas.column("Grado", width=150)
        self.lista_asignaturas.column("Asignatura", width=250)
        self.lista_asignaturas.pack(fill="both", pady=(0, 10))

        # Botón para agregar asignatura
        self.btn_agregar = cus.CTkButton(self, text="Agregar asignatura", command=self.mostrar_agregar)
        self.btn_agregar.pack(pady=10)

        # Botón para actualizar la lista
        self.btn_actualizar = cus.CTkButton(self, text="Actualizar asignaturas", command=self.actualizar_lista)
        self.btn_actualizar.pack(pady=10)

        # Cargar asignaturas iniciales
        self.crear_tabla_asignaturas()
        self.actualizar_lista()

    def crear_tabla_asignaturas(self):
        conn = sqlite3.connect("ges.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS asignaturas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       grado TEXT)""")
        conn.commit()
        conn.close()

    def actualizar_lista(self, grado=None):
        if not grado:
            grado = self.grado_combo.get()

        conn = sqlite3.connect("ges.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM asignaturas WHERE grado = ?", (grado,))
        asignaturas = cursor.fetchall()
        conn.close()

        # Limpiar las filas previas
        for row in self.lista_asignaturas.get_children():
            self.lista_asignaturas.delete(row)

        # Insertar las nuevas filas
        for nombre in asignaturas:
            self.lista_asignaturas.insert("", "end", values=(grado, nombre[0]))

    def mostrar_agregar(self):
        ventana = cus.CTkToplevel(self)
        ventana.geometry("300x150")

        cus.CTkLabel(ventana, text="Nombre de la asignatura")
        entry_nombre = cus.CTkEntry(ventana)
        entry_nombre.pack(pady=5)

        def agregar():
            nombre = entry_nombre.get()
            grado = self.grado_combo.get()

            if nombre:
                conn = sqlite3.connect("ges.db")
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO asignaturas (nombre, grado)
                    VALUES (?, ?)
                """, (nombre, grado))
                conn.commit()
                conn.close()

                self.actualizar_lista(grado)
                ventana.destroy()

        cus.CTkButton(ventana, text="Guardar", command=agregar).pack(pady=10)
