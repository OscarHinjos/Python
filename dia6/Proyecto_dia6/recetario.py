from bienvenida import *
from eleccion_usuario import *

if __name__ == "__main__":
    salir_programa = False
    bienvenida_usuario()
    while not salir_programa:
        eleccion = eleccion_usuario()
        if eleccion == 1:
            leer_receta()
        elif eleccion == 2:
            crear_receta()
        elif eleccion == 3:
            crear_categoria()
        elif eleccion == 4:
            eliminar_receta()
        elif eleccion == 6:
            print("Hasta pronto")
            salir_programa = True

