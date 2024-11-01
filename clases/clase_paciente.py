from interfaz_usuario.medicamento_GUI import medicamento_GUI
from interfaz_usuario.sintoma_GUI import sintoma_GUI
from interfaz_usuario.registros_GUI import registros_GUI


class paciente:
    def __init__(self, nombre, apellido):
        self.nombreCompleto = f'{nombre} {apellido}'
        self.registros_paciente = []

    def agregar_registro(self, registro):
        self.registros_paciente.append(registro)


    def agregar_paciente_combobox(self, paciente):
        sintoma_GUI.nombres_pacientes_comboBox.append(paciente.nombreCompleto)
        medicamento_GUI.nombres_pacientes_comboBox.append(paciente.nombreCompleto)
        registros_GUI.nombres_pacientes_comboBox.append(paciente.nombreCompleto)

        self.lista_pacientes(paciente)

    def lista_pacientes(self, paciente):
        sintoma_GUI.instancias_pacientes.append(paciente)
        medicamento_GUI.instancias_pacientes.append(paciente)
        registros_GUI.instancias_pacientes.append(paciente)