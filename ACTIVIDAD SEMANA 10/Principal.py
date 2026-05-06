from Numero_modelo import Numero
from Vista_formulario import VistaFormulario
from Controlador import Controlador




def main():
    modelo = Numero()
    vista = VistaFormulario()
    controlador = Controlador(modelo, vista)

    controlador.tomar_numero()
    controlador.imprimir_numero()


if __name__ == "__main__":
    main()