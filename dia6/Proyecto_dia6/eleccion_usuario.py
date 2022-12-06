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
    categorias = os.listdir(RUTA_PRINCIPAL)
    for i, categoria in enumerate(categorias):
        print(f"[{i + 1}] - {categoria}")
    escoger = int(input("Escoge una categoria: "))
    if escoger > len(categorias):
        print("Intentalo de nuevo")
        elegri_categoria()
    else:
        return escoger, categorias


def leer_receta():
    escoger, categorias = elegri_categoria()
    for i, categoria in enumerate(categorias):
        if escoger == i + 1:
            ruta = Path(RUTA_PRINCIPAL, categoria)
            for j, txt in enumerate(ruta.glob("*.txt")):
                print(f"[{j + 1}] - {os.path.basename(txt)}")


def crear_receta():
    escoger, categorias = elegri_categoria()
    nombre_receta = input("\nEscoge un nombre para la receta: \n")
    contenido = input("Contenido de el archivo: ")
    for i, categoria in enumerate(categorias):
        if escoger == i + 1:
            file = open(Path(RUTA_PRINCIPAL, categoria, nombre_receta), 'w', encoding='UTF-8')
            file.write(contenido)
            file.close()


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
    escoger, categorias = elegri_categoria()
    for i, categoria in enumerate(categorias):
        if escoger == i + 1:
            ruta = Path(RUTA_PRINCIPAL, categoria)
            for j , txt in enumerate(ruta.glob("*.txt")):
                print(f"[{j + 1}] - {os.path.basename(txt)}")
            escoger_receta = int(input("Escoge una receta para borrar: "))
            if escoger_receta > len(categoria) or escoger_receta < 0:
                escoger_receta = int(input("numero fuera de rango intentalo de nuevp: "))
            for y,txt2 in enumerate(ruta.glob("*.txt")):
                if escoger_receta == y + 1:
                    os.remove(Path(RUTA_PRINCIPAL, categoria, txt2))

def eliminar_categoria():
    escoger , categorias = elegri_categoria()
    for i , categoria in enumerate(categorias):
        if escoger == i + 1 :
            os.rmdir(Path(RUTA_PRINCIPAL, categoria))