"""
    Escoger una palabra secreta y mostrar una serie de guiones
    representa la cantidad de letras que tiene la palabra
"""

from random import *

salir = False
lista_Palabras = ['Foca', 'Loro', 'Polilla']


def palabra_aleatoria(lista_palabras):
    return choice(lista_palabras)


def guiones_palabra(palabra):
    lista_letras = list(palabra)
    lista_guiones = []
    for letra in range(len(lista_letras)):
        lista_guiones.append("_")

    return lista_guiones


def detectar_palabra(palabra, palabra_guiones):
    letra_usuario = pedir_info()
    lista_index = []
    palabra_guiones = palabra_guiones
    for i,letra in enumerate(palabra):
        if letra_usuario == letra:
            lista_index.append(i)

    for i,guion in enumerate(palabra_guiones):
        if i in lista_index:
            palabra_guiones[i] = letra_usuario


    return palabra_guiones






def pedir_info():
    letra = input("Dame una letra").lower()
    abecedario = "abcchdefghijklmnñopqrstuvwxyz"
    if len(letra) > 1 or not letra in abecedario or len(letra) < 0:
        print("Me diste mas de una letra o no escribiste una letra, intentalo de nuevo")
        pedir_info()
    return letra


if __name__ == "__main__":
    palabra = palabra_aleatoria(lista_Palabras).lower()
    print("Averigual la palabra".center(50,"-"))
    palabra_guiones = guiones_palabra(palabra)
    print(palabra_guiones)
    palabra_averiguada = ""
    lista_palabra = list(palabra)

    while salir == False:
        detectar = detectar_palabra(palabra, palabra_guiones)
        print(detectar)
        palabra_averiguada = "".join(detectar)
        if palabra_averiguada == palabra:
            print("Felicidades averiguaste la palabra")
            print(f"La palabra era {palabra_averiguada.capitalize()}")
            salir = True





