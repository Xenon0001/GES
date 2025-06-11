import customtkinter as cus
import tkinter as tk


class Menu(cus.CTkFrame):
    def __init__(self, master, callback, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = "gray7", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.callback = callback
        
        self.botones()

        self.place(x=0, y=0, relwidth=0.12, relheight=1)
    
    def botones(self):
        frame_top = cus.CTkFrame(self, height=50, fg_color="transparent")
        frame_main = cus.CTkFrame(self, height=150, fg_color="transparent")
        frame_bottom = cus.CTkFrame(self, fg_color="transparent")

        frame_top.pack()
        frame_main.pack(expand=True, fill="x")
        frame_bottom.pack(expand=True, fill="both")

        botones_menu = ["Panel", "Estudiantes", "Profesores", "Asignaturas"]

        for i in botones_menu:
            btn = cus.CTkButton(frame_main, text=i, height=30, fg_color="transparent", hover_color="gray15", command=lambda t=i:self.callback(t))
            btn.pack(expand=True, fill="x", pady=5)

        btn_ajustes = cus.CTkButton(frame_bottom, height=30, fg_color="transparent", anchor="center")
        btn_ajustes.pack(expand=True, fill="x", pady=5, side="bottom", anchor="center")