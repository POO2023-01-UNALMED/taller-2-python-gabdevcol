class Auto():
    def init(self, modelo = str(), precio = int(), asientos = [], marca = str(), motor = None, registro = int(), cantidadCreados = int()):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados
        self.asientos += Asiento
        self.motor = Motor

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
    def init(self, color = str(), precio = int(), registro = int()):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        coloresPermitidos = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        colorminuscula = color.lower()
        if colorminuscula in coloresPermitidos:
            self.color = color


class Motor():
    def init(self, numeroCilindros = int(), tipo = str(), registro = int()):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipominuscula = tipo.lower()
        if tipominuscula == 'electrico' or tipominuscula == 'gasolina':
            self.tipo = tipo





