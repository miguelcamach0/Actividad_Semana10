class Controlador:
    def __init__(self, modelo, vista):
        self.obj_numero = modelo
        self.obj_vista = vista

    def tomar_numero(self):
        numero = self.obj_vista.pedir_numero()
        self.obj_numero.set_numero(numero)

    def imprimir_numero(self):
        numero = self.obj_numero.get_numero()
        tipo = self.obj_numero.tipo_numero()
        paridad = "par" if self.obj_numero.es_par() else "impar"

        self.obj_vista.imprimir_numero(numero)
        self.obj_vista.imprimir_mensaje(f"El número es {tipo} y {paridad}.")