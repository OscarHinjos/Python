def depositar_o_retirar():
    escoger = int(input("[1] - Depositar\n"
                        "[2] - Retirar\n"
                        "[3] - Salir\n"
                        "Escoge una opcion: "))
    if escoger < 1 or escoger > 3:
        print("Accion no valida, vuelva a intentarlo")
        depositar_o_retirar()
    else:
        return escoger



