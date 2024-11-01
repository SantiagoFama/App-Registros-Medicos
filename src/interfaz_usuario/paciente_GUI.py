import customtkinter as ctk
from src.clases.clase_paciente import paciente


class paciente_GUI:
    def __init__(self, app):
        self.frame = ctk.CTkFrame(app)
        self.frame.pack(anchor='n', padx=20, pady=20, expand=False)

        labelTitulo = ctk.CTkLabel(self.frame, text='Crear Paciente', font=('Consolas', 16))
        labelTitulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        labelNombre = ctk.CTkLabel(self.frame, text='Nombre:')
        labelNombre.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        labelApellido = ctk.CTkLabel(self.frame, text='Apellido:')
        labelApellido.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        # ------------------------------------------- Entry ----------------------------

        self.entryNombre = ctk.CTkEntry(self.frame)
        self.entryNombre.grid(row=1, column=1, padx=10, pady=10)

        self.entryApellido = ctk.CTkEntry(self.frame)
        self.entryApellido.grid(row=2, column=1, padx=10, pady=10)

        # --------------------------------------------- Botón ----------------------------------

        boton = ctk.CTkButton(self.frame, text='Registrar', command=self.devolver_paciente)
        boton.grid(row=5, column=0, columnspan=2, pady=20)


    def limpiar_campos(self):
        self.entryNombre.delete(0, ctk.END)
        self.entryApellido.delete(0, ctk.END)


    def devolver_paciente(self):
        nombre = self.entryNombre.get()
        apellido = self.entryApellido.get()

        nuevo_paciente = paciente(nombre, apellido)
        nuevo_paciente.agregar_paciente_combobox(nuevo_paciente)

        self.limpiar_campos()

    def devolver_frame(self):
        return self.frame

