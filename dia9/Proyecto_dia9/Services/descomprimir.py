import zipfile


def descomprimir_archivo():
    my_zip = zipfile.ZipFile('archivos/Proyecto+Dia+9.zip', 'r')
    my_zip.extractall('archivos')
