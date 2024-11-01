class clase_sintoma:
    def __init__(self, sintoma, fecha, hora):
        self.sintoma = sintoma
        self.fecha = fecha
        self.hora = hora

    def mostrar_registro(self):
        return f'Medicamento: {self.sintoma}, el día {self.fecha} a las {self.hora}'




