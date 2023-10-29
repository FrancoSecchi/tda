
class ExeptionGrafo(Exception):
    def __init__(self, mensaje="Ha ocurrido un error"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)