class clase_medicamento:
    def __init__(self, medicamento, fecha, hora):
        self.medicamento = medicamento
        self.fecha = fecha
        self.hora = hora

    def mostrar_registro(self):
        return f'Medicamento: {self.medicamento}, el día {self.fecha} a las {self.hora}'
