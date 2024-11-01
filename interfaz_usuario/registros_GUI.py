import customtkinter as ctk


class registros_GUI:

    nombres_pacientes_comboBox = []
    instancias_pacientes = []


    def __init__(self, aplicacion):
        self.frame = ctk.CTkFrame(aplicacion)
        self.frame.pack(anchor='n', padx=20, pady=20, expand=False)

        # --------------------------------------------- Combobox -------------------------------------------------------

        self.combo_var = ctk.StringVar(value='Elegir paciente')
        self.combo = ctk.CTkOptionMenu(self.frame, variable=self.combo_var, values=self.nombres_pacientes_comboBox, command=self.actualizar_registros)
        self.combo.pack(side='top', anchor='n',pady=(10, 20))


    def actualizar_registros(self, nada=None):
        paciente = self.combo.get()
        self.borrar_registros()

        for nombre in self.nombres_pacientes_comboBox:
            if nombre == paciente:
                for pac in self.instancias_pacientes:
                    if pac.nombreCompleto == nombre:
                        for reg in pac.registros_paciente:
                            texto_registro = reg.mostrar_registro()
                            label = ctk.CTkLabel(self.frame, text=texto_registro)
                            label.pack(anchor="w", padx=10, pady=5)


    def borrar_registros(self):
        for label in self.frame.winfo_children():
            if label == self.combo:
                pass
            else: label.destroy()


    def devolver_frame(self):
        return self.frame

    def actualizar_combo(self):
        self.combo.configure(values=self.nombres_pacientes_comboBox)