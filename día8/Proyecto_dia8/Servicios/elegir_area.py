def elegir_area():
    area = int(input("[1]-Perfumeria\n"
                     "[2]-Farmacia\n"
                     "[3]-Cosmeticos\n"
                     "[4]-Dejar de coger turnos\n"
                     "Escoge una opcion : "))
    if area < 1 or area > 4:
        print("No has escogido una opcion correcta, vuelve a intentarlo")
        area
    else:
        return area
