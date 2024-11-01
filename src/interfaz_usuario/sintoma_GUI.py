import customtkinter as ctk
from tkcalendar import *
import tkinter as ttk

from src.clases.clase_sintoma import clase_sintoma

class sintoma_GUI:

    nombres_pacientes_comboBox = []
    instancias_pacientes = []

    def __init__(self, aplicacion):
        self.frame = ctk.CTkFrame(aplicacion)
        self.frame.pack(anchor='n', padx=20, pady=20, expand=False)

        # ------------------------------------------- Labels -----------------------------------------------------------

        labelTitulo = ctk.CTkLabel(self.frame, text='Registrar Síntoma', font=('Consolas', 16))
        labelTitulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.label1 = ctk.CTkLabel(self.frame, text='Síntoma:')
        self.label1.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.label2 = ctk.CTkLabel(self.frame, text='Fecha:')
        self.label2.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.label3 = ctk.CTkLabel(self.frame, text='Hora:')
        self.label3.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        self.label4 = ctk.CTkLabel(self.frame, text='Paciente:')
        self.label4.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        # ------------------------------------------- Entry ------------------------------------------------------------

        self.entrySintoma = ctk.CTkEntry(self.frame)
        self.entrySintoma.grid(row=1, column=1)

        self.fecha = DateEntry(self.frame, date_pattern='dd-mm-yyyy')
        self.fecha.grid(row=2, column=1)

        self.hora = ttk.Spinbox(self.frame, from_=0, to=23, width=4)
        self.hora.grid(row=3, column=0, columnspan=2)

        self.minuto = ttk.Spinbox(self.frame, from_=0, to=59, width=4)
        self.minuto.grid(row=3, column=1, columnspan=3)

        # --------------------------------------------- Combobox -------------------------------------------------------

        self.var = ctk.StringVar(value='Elegir paciente')
        self.combo = ctk.CTkOptionMenu(self.frame, variable= self.var, values=self.nombres_pacientes_comboBox)
        self.combo.grid(row=4, column=1, padx=5, columnspan=3)

        # --------------------------------------------- Botón ----------------------------------------------------------

        boton = ctk.CTkButton(self.frame, text='Registrar', command= self.obtener_valor)
        boton.grid(row=5, column=0, columnspan=2, pady=20)


    def obtener_valor(self):
        sintoma = self.entrySintoma.get()
        fecha = self.fecha.get()
        hora = self.hora.get()
        minutos = self.minuto.get()
        hora_total = f'{hora}:{minutos}'

        registro = clase_sintoma(sintoma, fecha, hora_total)

        nombrePaciente = self.combo.get()

        for paciente in self.instancias_pacientes:
            if nombrePaciente == paciente.nombreCompleto:
                paciente.agregar_registro(registro)

        self.limpiar_campos()

    def limpiar_campos(self):
        self.entrySintoma.delete(0, ctk.END)
        self.fecha.delete(0, ctk.END)

    def devolver_frame(self):
        return self.frame

    def actualizar_combo(self):
        self.combo.configure(values=self.nombres_pacientes_comboBox)

