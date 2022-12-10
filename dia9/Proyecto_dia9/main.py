from Services.descomprimir import *
from Services.Buscador_numeros import *
from Services.date_today import *
if __name__ == "__main__":
    descomprimir_archivo()
    dict_num_series = encontrar_num_series()
    print(f"Fecha de busqueda [{today()}]")
    listar_num_series(dict_num_series)