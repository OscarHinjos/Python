import os
from pathlib import *


def bienvenida_usuario():
    print("Bienvenido al recetario")
    print(recetas_ubicacion())
    print(f"Tienes {cantidad_recetas()} recetas")


def recetas_ubicacion():
    return Path(os.getcwd(), 'Recetas')


def cantidad_recetas():
    ruta = Path(os.getcwd(), 'Recetas')
    ruta_carne = Path(ruta, 'Carnes')
    cantidad_recetas_carne = 0
    ruta_ensalada = Path(ruta, 'Ensaladas')
    cantidad_recetas_ensaladas = 0
    ruta_pastas = Path(ruta, 'Pastas')
    cantidad_recetas_pasta = 0
    ruta_postre = Path(ruta, 'Postres')
    cantidad_recetas_postres = 0

    for i,txt in enumerate(ruta_carne.glob("*.txt")):
        cantidad_recetas_carne += 1
    for i, txt in enumerate(ruta_ensalada.glob("*.txt")):
        cantidad_recetas_ensaladas += 1
    for i, txt in enumerate(ruta_pastas.glob("*.txt")):
        cantidad_recetas_pasta += 1
    for i, txt in enumerate(ruta_postre.glob("*.txt")):
        cantidad_recetas_postres += 1


    return cantidad_recetas_carne + cantidad_recetas_ensaladas + cantidad_recetas_pasta + cantidad_recetas_postres


