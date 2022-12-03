from pathlib import Path
import os

RUTA_PRINCIPAL = Path(os.getcwd(), 'Recetas')


def eleccion_usuario():
    try:
        eleccion = int(input("[1] - Leer receta\n"
                             "[2] - Crear receta\n"
                             "[3] - Crear categoria\n"
                             "[4] - Eliminar receta\n"
                             "[5] - Eliminar categoria\n"
                             "[6] - Finalizar programa\n"
                             "Elige una opcion: "))
        if eleccion < 1 or eleccion > 6:
            print("Escogiste un número fuera de trango intentalo de nuevo porfavor")
            eleccion_usuario()
        else:
            return eleccion
    except Exception as e:
        print("Caracter invalido")


def leer_receta():
    categoria = int(input("[1] - Carne\n"
                          "[2] - Ensaladas\n"
                          "[3] - Pastas\n"
                          "[4] - Postres\n"
                          "Elige una opcion: "))
    if categoria == 1:
        ruta_carne = Path(RUTA_PRINCIPAL, 'Carnes')
        for i,txt in enumerate(ruta_carne.glob("*.txt")):
            print(f"[{i+1}] - {os.path.basename(txt)}")

        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i,txt in enumerate(ruta_carne.glob("*.txt")):
            if elegir_receta == i:
                file = open(txt, 'r', encoding='UTF-8')
                print(file.read())