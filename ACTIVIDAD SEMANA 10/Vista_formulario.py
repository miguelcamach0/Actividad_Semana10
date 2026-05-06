class VistaFormulario:
    def __init__(self):
        self.titulo = "Programa de Números"
        self.pregunta_campo_numero = "Ingrese un número: "

    def pedir_numero(self):
        while True:
            try:
                return int(input(self.pregunta_campo_numero))
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

    def imprimir_mensaje(self, mensaje):
        print(mensaje)

    def imprimir_numero(self, numero):
        print(f"Número ingresado: {numero}")