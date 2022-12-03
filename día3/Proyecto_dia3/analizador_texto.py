lista_letras = []
texto = input("Escribe lo que quieras\n")
texto_lower = texto.lower()
letra1 = input("Escribe una primera letra\n")
letra2 = input("Escribe una segunda letra\n")
letra3 = input("Escribe una tercera letra\n")

lista_letras.append(letra1.lower())
lista_letras.append(letra2.lower())
lista_letras.append(letra3.lower())

print(f"Elegiste las letras {lista_letras}")

# Analisis
# Cuantas veces aparece cada una de las letras que eligio

aparicion_letra1 = texto_lower.count(lista_letras[0])
aparicion_letra2 = texto_lower.count(lista_letras[1])
aparicion_letra3 = texto_lower.count(lista_letras[2])

print(f"La letra {letra1}, aparece {aparicion_letra1} veces")
print(f"La letra {letra2}, aparece {aparicion_letra2} veces")
print(f"La letra {letra3}, aparece {aparicion_letra3} veces")

# Cuantas palabras hay en total

texto_lista = texto.split(" ")
print(f"La cantidad de palabras en total es de: {len(texto_lista)} ")

# Localizar la ultima y la primera letra

print(f"La letra {texto[0]} es la primera del texto")
print(f"La letra {texto[-1]} es la primera del texto")

# Invertir el orden de las palabras

print(f"El orden inverso del texto seria:\n'{texto[::-1]}'")

# Aparece la palabra python

python = "python"

if python in texto_lower:
    print(f"La palabra {python} aparece en el texto")
else:
    print(f"La palabra {python} no aparece en el texto")

