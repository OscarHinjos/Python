from dia10.Services.enemigo import *
from random import *
from time import *


def list_enemigos():
    cantidad = randint(1, 10)
    nombre = 'enemigo'
    lst_enemigo = []
    for c in range(cantidad):
        nombre_enemigo = nombre + str(c)
        nombre_enemigo = Enemigo(randint(0, 736), randint(50, 200))
        lst_enemigo.append(nombre_enemigo)

    return lst_enemigo


