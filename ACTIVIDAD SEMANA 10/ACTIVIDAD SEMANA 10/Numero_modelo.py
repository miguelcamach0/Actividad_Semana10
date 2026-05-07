class Numero:
    def __init__(self):
        self.dato_numero = 0

    def get_numero(self):
        return self.dato_numero

    def set_numero(self, nuevo_numero):
        self.dato_numero = nuevo_numero

    def es_par(self):
        return self.dato_numero % 2 == 0

    def tipo_numero(self):
        if self.dato_numero > 0:
            return "positivo"
        elif self.dato_numero < 0:
            return "negativo"
        else:
            return "neutro"