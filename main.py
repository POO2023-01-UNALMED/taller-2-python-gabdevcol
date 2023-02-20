class Auto():
    cantidadCreados = int()
    def init(self):
        self.modelo = str()
        self.precio = int()
        self.asientos = list()
        self.marca = str()
        self.motor = Motor()
        self.registro = int()

    def cantidadAsientos(self):
        cantidad = len(self.asientos)
        return cantidad

    def verificarIntegridad(self):
        mensaje = "Auto original"
        if self.motor.registro == self.registro:
            for asiento in self.asientos:
                if asiento.registro != self.registro:
                    mensaje = "Las piezas no son originales"
                    break

        else:
            mensaje = "Las piezas no son originales"

        return mensaje


class Asiento():
    def init(self):
        self.color = str()
        self.precio = int()
        self.registro = int()

    def cambiarColor(self, color):
        coloresPermitidos = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        colorminuscula = color.lower()
        if colorminuscula in coloresPermitidos:
            self.color = color


class Motor():
    def init(self):
        self.numeroCilindros = int()
        self.tipo = str()
        self.registro = int()

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipominuscula = tipo.lower()
        if tipominuscula == 'electrico' or tipominuscula == 'gasolina':
            self.tipo = tipo





