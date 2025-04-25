import customtkinter as cus


class Subjects(cus.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=20, pady=20, fill="both", expand=True)

        # Titulo
        self.label = cus.CTkLabel(self, text="Asignaturas", font=("Arial", 24))
        self.label.pack(pady=(10, 20))

        # Selecciçon de grado
        self.grado_combo = cus.CTkComboBox(self, values=[
            "1º Primaria", "2º Primaria", "3º Primaria", "4º Primaria",
            "5º Primaria", "6º Primaria", "1º Eso", "2º Eso", "3º Eso",
            "4º Eso", "1º Bachillerato", "2º Bachillerato"
        ])
        self.grado_combo.set("1º Primaria")
        self.grado_combo.pack(fill="x", pady=(0, 10))

        # Lista e asignaturas
        self.lista_asignaturas = cus.CTkTextbox(self, height=150)
        self.lista_asignaturas.insert("0.0", "Matemáticas\nLengua")
        self.lista_asignaturas.configure(state="disabled")
        self.lista_asignaturas.pack(fill="both", pady=(0, 10))

        # Boton para agregar
        self.btn_agregar = cus.CTkButton(self, text="Agregar asignatura", command=self.mostrar_agregar)
        self.btn_agregar.pack()

    def mostrar_agregar(self):
        ventana = cus.CTkToplevel(self)
        ventana.geometry("300x150")

        cus.CTkLabel(ventana, text="Nombre de la asignatura")
        entry_nombre = cus.CTkEntry(ventana)
        entry_nombre.pack(pady=5)

        def agregar():
            nombre = entry_nombre.get()
            if nombre:
                self.lista_asignaturas.configure(state="normal")
                self.lista_asignaturas.insert("end", f"\n{nombre}")
                self.lista_asignaturas.configure(state="disabled")
                ventana.destroy()
        
        cus.CTkButton(ventana, text="Guardar", command=agregar).pack(pady=10)
