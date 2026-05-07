from Numero_modelo import Numero
from Vista_formulario import VistaFormulario
from Controlador import Controlador

def main():

    modelo = Numero()

    vista = VistaFormulario()

    controlador = Controlador(modelo, vista)

    # Conectar botón con controlador
    vista.boton.config(command=controlador.procesar_numero)

    vista.iniciar()

if __name__ == "__main__":
    main()