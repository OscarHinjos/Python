
from Services.cantidad import *
from Services.escoger import *
from Services.crear_cliente import *

if __name__ == "__main__":
    cliente = crear_cliente()
    salir = False
    while not salir:
        print(cliente)
        escoger = depositar_o_retirar()
        if escoger == 1:
            cliente.depositar(cantidad())
        elif escoger == 2:
            cliente.retirar(cantidad())
        elif escoger == 3:
            print("Hasta pronto")
            salir = True



