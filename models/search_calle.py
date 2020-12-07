import re
import os

file_txt = 'calles_text_list.txt'

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
ruta = os.path.join(basedir, file_txt)
print(ruta)


def sin_tilde(nombre_calle):
    return nombre_calle.translate(str.maketrans("ÁÉÍÓÚ", "AEIOU"))


def calle_txt(nombre_calle=None):
    file_txt = ruta
    calle_info = []

    print(nombre_calle)
    nombre_calle = (' ').join(nombre_calle.split('_'))
    #print('Despues Split', nombre_calle)
    nombre_calle = f'{nombre_calle.upper()}'
    #print("Despues de (calle)", nombre_calle)
    nombre_calle = sin_tilde(nombre_calle)
    print("NOMBRE CALLE", nombre_calle)

    pattern = re.compile(r"({0} \(calle\)|{0} \(avenida\))".format(nombre_calle))

    #(CRAMER \(calle\)|CRAMER \(avenida\))
    with open(file_txt, encoding='latin1') as openfile:
        index_1 = 0
        for linea in openfile:

            if pattern.search(linea) is not None:
                index_1 = 1

            if index_1 == 1:
                if nombre_calle.lower().title() in linea:
                    linea = linea.replace('- ', '')
                    linea = linea.replace('', '"').replace('', '"')
                    calle_info.append(linea.strip())
                    break

    if calle_info:
        print(calle_info)
        return calle_info[0]

    return calle_info
