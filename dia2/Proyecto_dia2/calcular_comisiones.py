
nombre = input("¿Como te llamas?\n")
ventas_totales = float(input("¿Cuanto has vendido el día de hoy?\n"))

calcular_comision = ventas_totales * 0.13

print(f"Hola {nombre} tu comision por lo vendido es de: {round(calcular_comision, 2)} euros")