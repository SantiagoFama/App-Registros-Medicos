import customtkinter as ctk
from tkcalendar import *
import tkinter as ttk

from clases.clase_medicamento import clase_medicamento

class medicamento_GUI:

    nombres_pacientes_comboBox = []
    instancias_pacientes = []

    def __init__(self, app):
        self.frame = ctk.CTkFrame(app)
        self.frame.pack(anchor='n', padx=20, pady=20, expand=False)

        # ------------------------------------------- Labels -----------------------------------------------------------

        labelTitulo = ctk.CTkLabel(self.frame, text='Registrar Medicamento', font=('Consolas', 16))
        labelTitulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.label1 = ctk.CTkLabel(self.frame, text='Medicamento:')
        self.label1.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.label2 = ctk.CTkLabel(self.frame, text='Fecha:')
        self.label2.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.label3 = ctk.CTkLabel(self.frame, text='Hora:')
        self.label3.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        self.label4 = ctk.CTkLabel(self.frame, text='Paciente:')
        self.label4.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        # ------------------------------------------- Entry ------------------------------------------------------------

        self.entryMedicamento = ctk.CTkEntry(self.frame)
        self.entryMedicamento.grid(row=1, column=1)

        self.fecha = DateEntry(self.frame, date_pattern='dd-mm-yyyy')
        self.fecha.grid(row=2, column=1)

        self.hora = ttk.Spinbox(self.frame, from_=0, to=23, width=4)
        self.hora.grid(row=3, column=0, columnspan=2)

        self.minuto = ttk.Spinbox(self.frame, from_=0, to=59, width=4)
        self.minuto.grid(row=3, column=1, columnspan=3)

        # --------------------------------------------- Combobox -------------------------------------------------------

        self.var = ctk.StringVar(value='Elegir paciente')
        self.combo = ctk.CTkOptionMenu(self.frame, variable= self.var,values=self.nombres_pacientes_comboBox)
        self.combo.grid(row=4, column=1, padx=5, columnspan=3)

        # --------------------------------------------- Botón ----------------------------------------------------------

        boton = ctk.CTkButton(self.frame, text='Crear', command=self.obtener_valor)
        boton.grid(row=5, column=0, columnspan=2, pady=20)

    def obtener_valor(self):
        medicamento = self.entryMedicamento.get()
        fecha_medicamento = self.fecha.get()
        hora = self.hora.get()
        minuos = self.minuto.get()
        hora_total = f'{hora}:{minuos}'

        registro = clase_medicamento(medicamento, fecha_medicamento, hora_total)

        paciente_combobox = self.combo.get()

        for paciente in self.instancias_pacientes:
            if paciente_combobox == paciente.nombreCompleto:
                paciente.agregar_registro(registro)
                print('registrado')

        self.limpiar_campos()

    def limpiar_campos(self):
        self.entryMedicamento.delete(0, ctk.END)
        self.fecha.delete(0, ctk.END)

    def devolver_frame(self):
        return self.frame

    def actualizar_combo(self):
        self.combo.configure(values=self.nombres_pacientes_comboBox)