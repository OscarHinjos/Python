from día8.Proyecto_dia8.Establecimientos.Cliente import *


def datos_cliente(turno):
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    turno_cliente = turno

    cliente = Cliente(nombre, apellidos, turno_cliente)

    return cliente
