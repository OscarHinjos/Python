from bienvenida import *
from eleccion_usuario import *

if __name__ == "__main__":
    salir_programa = False
    bienvenida_usuario()
    while not salir_programa:
        eleccion = eleccion_usuario()
        if eleccion == 1:
            leer_receta()
        if eleccion == 2:
            pass
        elif eleccion == 6:
            print("Hasta pronto")
            salir_programa = True

