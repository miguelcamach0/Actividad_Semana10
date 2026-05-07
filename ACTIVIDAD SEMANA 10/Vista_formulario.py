import tkinter as tk

class VistaFormulario:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Analizador de Números")
        self.ventana.geometry("500x350")
        self.ventana.configure(bg="#dff6ff")

        # TÍTULO
        self.label_titulo = tk.Label(
            self.ventana,
            text="ANALIZADOR DE NÚMEROS",
            font=("Arial", 18, "bold"),
            bg="#dff6ff",
            fg="#003566"
        )

        self.label_titulo.pack(pady=20)

        # INSTRUCCIÓN
        self.label_numero = tk.Label(
            self.ventana,
            text="Ingrese un número:",
            font=("Arial", 12),
            bg="#dff6ff"
        )

        self.label_numero.pack(pady=10)

        # CAMPO DE TEXTO
        self.entry_numero = tk.Entry(
            self.ventana,
            font=("Arial", 14),
            justify="center",
            width=15
        )

        self.entry_numero.pack(pady=10)

        # BOTÓN
        self.boton = tk.Button(
            self.ventana,
            text="Analizar Número",
            font=("Arial", 12, "bold"),
            bg="#0077b6",
            fg="white",
            padx=10,
            pady=5
        )

        self.boton.pack(pady=20)

        # RESULTADO
        self.label_resultado = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 13, "bold"),
            bg="#dff6ff",
            fg="#03045e"
        )

        self.label_resultado.pack(pady=20)

    def obtener_numero(self):
        return self.entry_numero.get()

    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)

    def iniciar(self):
        self.ventana.mainloop()