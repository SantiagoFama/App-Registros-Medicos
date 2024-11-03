from src.interfaz_usuario.medicamento_GUI import medicamento_GUI
from src.interfaz_usuario.sintoma_GUI import sintoma_GUI
from src.interfaz_usuario.registros_GUI import registros_GUI

import json

class paciente:

    datos = {
        "pacientes": [],
        "sintomas": [
            {
                "fecha": [],
                "hora": [],
                "paciente": [],
                "sintoma": [],
            }
        ],
        "medicamentos": [
            {
                "fecha": [],
                "hora": [],
                "paciente": [],
                "medicamento": [],
            }
        ]
    }

    def __init__(self, nombre, apellido):
        self.nombreCompleto = f'{nombre} {apellido}'
        self.registros_paciente = []


    def guardar_datos(self, fecha, hora, nombre, registro, tipo_registro):
        self.registros_paciente.append(registro)

        if tipo_registro == "medicamento":

            self.datos["pacientes"].append(self.nombreCompleto)
            self.datos["medicamentos"][0]["paciente"].append(self.nombreCompleto)

            self.datos["medicamentos"][0]["fecha"].append(fecha)
            self.datos["medicamentos"][0]["hora"].append(hora)
            self.datos["medicamentos"][0]["medicamento"].append(nombre)
            self.exportar_datos_json()

        elif tipo_registro == "sintoma":

            self.datos["pacientes"].append(self.nombreCompleto)
            self.datos["sintomas"][0]["paciente"].append(self.nombreCompleto)

            self.datos["sintomas"][0]["fecha"].append(fecha)
            self.datos["sintomas"][0]["hora"].append(hora)
            self.datos["sintomas"][0]["sintoma"].append(nombre)
            self.exportar_datos_json()


    def exportar_datos_json(self, filename="datos.json"):
        with open(filename, "w") as f:
            json.dump(self.datos, f, indent=4)


    def agregar_paciente_combobox(self, paciente):
        sintoma_GUI.nombres_pacientes_comboBox.append(paciente.nombreCompleto)
        medicamento_GUI.nombres_pacientes_comboBox.append(paciente.nombreCompleto)
        registros_GUI.nombres_pacientes_comboBox.append(paciente.nombreCompleto)

        self.lista_pacientes(paciente)


    def lista_pacientes(self, paciente):
        sintoma_GUI.instancias_pacientes.append(paciente)
        medicamento_GUI.instancias_pacientes.append(paciente)
        registros_GUI.instancias_pacientes.append(paciente)