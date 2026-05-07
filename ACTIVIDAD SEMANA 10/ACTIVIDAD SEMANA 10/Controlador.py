from tkinter import messagebox

class Controlador:

    def __init__(self, modelo, vista):
        self.obj_numero = modelo
        self.obj_vista = vista

    def procesar_numero(self):

        try:
            numero = int(self.obj_vista.obtener_numero())

            self.obj_numero.set_numero(numero)

            tipo = self.obj_numero.tipo_numero()

            paridad = "par" if self.obj_numero.es_par() else "impar"

            mensaje = f"El número {numero} es {tipo} y {paridad}."

            self.obj_vista.mostrar_resultado(mensaje)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese un número válido"
            )