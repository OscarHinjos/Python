import os
import re
from pathlib import Path
import time
import math
RUTA = 'archivos/Mi_Gran_Directorio'
expresion = r'[N]\w{3}[-]\d{5}'


def encontrar_num_series():
    num_serie_dict = {}
    for carpeta, sub, arch in os.walk(RUTA):
        rute = Path(carpeta)
        for rute_all in rute.glob("*.txt"):
            file = open(rute_all,'r')
            validate = re.findall(expresion,file.read())
            num_serie_dict[os.path.basename(rute_all)] = validate

    return num_serie_dict


def listar_num_series(num_serie_dict):
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    inicio = time.time()
    for key,value in num_serie_dict.items():
        if not len(value) == 0:
            for values in value:
                print(f"{key}\t{values}")
    final = time.time()
    print(f"Numeros encontrados: {len(values)}")
    print(f"La busqueda de numeros de serie a durado: {math.ceil(final-inicio)} segundos")



