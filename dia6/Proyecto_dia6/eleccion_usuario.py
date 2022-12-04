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

def elegri_categoria():
    categoria = int(input("[1] - Carne\n"
                          "[2] - Ensaladas\n"
                          "[3] - Pastas\n"
                          "[4] - Postres\n"
                          "Elige una opcion: "))
    return categoria
def leer_receta():
    categoria = elegri_categoria()
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
    elif categoria == 2:
        ruta_ensaladas = Path(RUTA_PRINCIPAL,'Ensaladas')
        for i,txt in enumerate(ruta_ensaladas.glob("*.txt")):
            print(f"[{i+1}] - {os.path.basename(txt)}")
        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i,txt in enumerate(ruta_ensaladas.glob("*.txt")):
            if elegir_receta == i:
                file = open(txt, 'r', encoding='UTF-8')
                print(file.read())
    elif categoria == 3:
        ruta_pastas = Path(RUTA_PRINCIPAL,'Pastas')
        for i,txt in enumerate(ruta_pastas.glob("*.txt")):
            print(f"[{i+1}] - {os.path.basename(txt)}")
        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i,txt in enumerate(ruta_pastas.glob("*.txt")):
            if elegir_receta == i:
                file = open(txt, 'r', encoding='UTF-8')
                print(file.read())

    elif categoria == 4:
        ruta_postres = Path(RUTA_PRINCIPAL,'Postres')
        for i,txt in enumerate(ruta_postres.glob("*.txt")):
            print(f"[{i+1}] - {os.path.basename(txt)}")
        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i,txt in enumerate(ruta_postres.glob("*.txt")):
            if elegir_receta == i:
                file = open(txt, 'r', encoding='UTF-8')
                print(file.read())

def crear_receta():
    categoria = elegri_categoria()
    nombre_receta = input("\nEscoge un nombre para la receta: \n")
    contenido = input("Contenido de el archivo: ")
    if categoria == 1:
        file = open(Path(RUTA_PRINCIPAL,'Carnes',nombre_receta),'w',encoding='UTF-8',)
        file.write(contenido)
    elif categoria == 2:
        file = open(Path(RUTA_PRINCIPAL,'Ensaladas',nombre_receta),'w',encoding='UTF-8')
        file.write(contenido)
    elif categoria == 3:
        file = open(Path(RUTA_PRINCIPAL,'Pastas',nombre_receta),'w',encoding='UTF-8')
        file.write(contenido)
    elif categoria == 2:
        file = open(Path(RUTA_PRINCIPAL,'Postres',nombre_receta),'w',encoding='UTF-8')
        file.write(contenido)

def crear_categoria():
    crear_cate = input("Nombre de la categoria que quieres crear: ")
    lista_categoria = os.listdir(RUTA_PRINCIPAL)
    for categoria in lista_categoria:
        if crear_cate in categoria:
            print("Lo sentimos la categoria ya ha sido creada, intentalo de nuevo")
            crear_categoria()
        else:
            os.makedirs(Path(RUTA_PRINCIPAL, crear_cate))
            break


def eliminar_receta():
    categoria = elegri_categoria()
    if categoria == 1:
        ruta_carne = Path(RUTA_PRINCIPAL, 'Carnes')
        for i, txt in enumerate(ruta_carne.glob("*.txt")):
            print(f"[{i + 1}] - {os.path.basename(txt)}")

        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i, txt in enumerate(ruta_carne.glob("*.txt")):
            if elegir_receta == i:
                os.remove(Path(ruta_carne, txt))
    elif categoria == 2:
        ruta_ensalada = Path(RUTA_PRINCIPAL, 'Ensaladas')
        for i, txt in enumerate(ruta_ensalada.glob("*.txt")):
            print(f"[{i + 1}] - {os.path.basename(txt)}")

        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i, txt in enumerate(ruta_ensalada.glob("*.txt")):
            if elegir_receta == i:
                os.remove(Path(ruta_ensalada, txt))
    elif categoria == 3:
        ruta_pastas = Path(RUTA_PRINCIPAL, 'Pastas')
        for i, txt in enumerate(ruta_pastas.glob("*.txt")):
            print(f"[{i + 1}] - {os.path.basename(txt)}")

        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i, txt in enumerate(ruta_pastas.glob("*.txt")):
            if elegir_receta == i:
                os.remove(Path(ruta_pastas, txt))
    elif categoria == 4:
        ruta_postres = Path(RUTA_PRINCIPAL, 'Pastas')
        for i, txt in enumerate(ruta_postres.glob("*.txt")):
            print(f"[{i + 1}] - {os.path.basename(txt)}")

        elegir_receta = int(input("Escoge una receta para ver: "))
        elegir_receta -= 1
        for i, txt in enumerate(ruta_postres.glob("*.txt")):
            if elegir_receta == i:
                os.remove(Path(ruta_postres, txt))
    else:
        print("Fallo al escoger categoria, vuelva a intentarlo")
        eliminar_receta()
    pass