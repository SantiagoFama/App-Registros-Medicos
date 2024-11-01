import customtkinter as ctk
from tkinter import StringVar

from src.interfaz_usuario.sintoma_GUI import sintoma_GUI
from src.interfaz_usuario.paciente_GUI import paciente_GUI
from src.interfaz_usuario.medicamento_GUI import medicamento_GUI
from src.interfaz_usuario.registros_GUI import registros_GUI


class GUI_principal:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry('400x400+250+40')                     # Tamaño
        self.app.title('Registro Enfermedades')                 # Título
        self.app.iconbitmap("interfaz_usuario/icono.ico")                        # Icono
        self.app.configure(bg='azure2')                         # Color de fondo

        self.frame_contenedor = ctk.CTkFrame(self.app)
        self.frame_contenedor.pack(fill='both', expand=True)

        self.inicializar_frames()
        self.crear_menu_opciones()
        self.mostrar_frame(self.seleccion.get())

        self.app.mainloop()

    def inicializar_frames(self):
        self.sintoma = sintoma_GUI(self.app)
        self.frame_sintoma = self.sintoma.devolver_frame()

        self.paciente = paciente_GUI(self.app)
        self.frame_paciente = self.paciente.devolver_frame()

        self.medicamento = medicamento_GUI(self.app)
        self.frame_medicamento = self.medicamento.devolver_frame()

        self.registros = registros_GUI(self.app)
        self.frame_registros = self.registros.devolver_frame()

    def crear_menu_opciones(self):
        opciones = ["Crear Paciente", "Registrar Síntoma", "Registrar Medicamento", "Registros"]
        self.seleccion = StringVar(value='Crear Paciente')

        self.option_menu = ctk.CTkOptionMenu(self.frame_contenedor, variable=self.seleccion, values=opciones, command=self.mostrar_frame)
        self.option_menu.pack(pady=10)

    def mostrar_frame(self, opcion):
        self.frame_paciente.pack_forget()
        self.frame_sintoma.pack_forget()
        self.frame_medicamento.pack_forget()
        self.frame_registros.pack_forget()

        if opcion == "Crear Paciente":
            self.frame_paciente.pack(fill='both', expand=True)

        elif opcion == "Registrar Síntoma":
            self.frame_sintoma.pack(fill='both', expand=True)
            self.sintoma.actualizar_combo()

        elif opcion == "Registrar Medicamento":
            self.frame_medicamento.pack(fill='both', expand=True)
            self.medicamento.actualizar_combo()

        elif opcion == "Registros":
            self.frame_registros.pack(fill='both', expand=True)
            self.registros.actualizar_combo()