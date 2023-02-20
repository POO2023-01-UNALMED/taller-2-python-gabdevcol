class Auto:
    cantidadCreados = int()
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        self.asientos.remove(None)
        cantidad = len(self.asientos)
        return cantidad

    def verificarIntegridad(self):
        mensaje = "Auto original"
        self.asientos.remove(None)
        if self.motor.registro == self.registro:
            for asiento in self.asientos:
                if asiento.registro != self.registro:
                    mensaje = "Las piezas no son originales"
                    break

        else:
            mensaje = "Las piezas no son originales"

        return mensaje


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        coloresPermitidos = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        colorminuscula = color.lower()
        if colorminuscula in coloresPermitidos:
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipominuscula = tipo.lower()
        if tipominuscula == 'electrico' or tipominuscula == 'gasolina':
            self.tipo = tipo





