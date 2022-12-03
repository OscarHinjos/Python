import random

nombre = input("¿Cual es tu nombre?\n")
numero_aleatorio = random.randint(1,100)
intentos = 8
contador = 0
print(f"Hola {nombre} he pensado un numero del 1 al 100\nTines {intentos} para lograrlo, cual crees que es el numero")

while contador < 8:
    numero_usuario = int(input("Dime un número"))
    print(f"Intentos restantes {intentos} intentos")
    if numero_usuario < 1 or numero_usuario > 100:
        print("Has elegido un número que no esta permitido")

    elif numero_usuario < numero_aleatorio:
        print("Has elegido un numero menor al numero secreto")

    elif numero_usuario > numero_aleatorio:
        print("Has elegido un numero mayor al numero secreto")
    elif numero_usuario == numero_aleatorio:
        print(f"Has acertado, enorabuena\nTe ha tomado {intentos}")
        break

    if intentos == 0:
        print("Lo siento has agotado tun intentos")
    intentos -= 1
    contador+= 1