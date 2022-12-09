import elegir_area as el
import datos_cliente as dt
from día8.Proyecto_dia8.Establecimientos.Perfumeria import *
from día8.Proyecto_dia8.Establecimientos.Farmacia import *
from día8.Proyecto_dia8.Establecimientos.Cosmeticos import *


def turnero():
    salir = False
    while not salir:
        elegir = el.elegir_area()
        if elegir == 1:
            print(dt.datos_cliente(next(Perfumeria.turnos())))
        elif elegir == 2:
            print(dt.datos_cliente(next(Farmacia.turnos())))
        elif elegir == 3:
            print(dt.datos_cliente(next(Cosmeticos.turnos())))
        elif elegir == 4:
            print("Hasta pronto")
            salir = True

turnero()