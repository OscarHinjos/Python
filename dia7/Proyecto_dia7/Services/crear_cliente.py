from random import *
from dia7.Proyecto_dia7.Clases.Cliente import *


def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = str(randint(100, 9999))
    balance = float(randint(1,5000))

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente
