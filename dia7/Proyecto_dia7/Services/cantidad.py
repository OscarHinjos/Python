def cantidad():
    cantidad_dinero = float(input("Dime una cantidad: "))
    if cantidad_dinero < 0:
        print("Numero fuera de rango, vuelva a intentarlo")
        cantidad()
    else:
        return cantidad_dinero