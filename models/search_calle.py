import re
import os

file_txt = 'calles_text_list.txt'

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
ruta = os.path.join(basedir, file_txt)
print(ruta)

# nombre_calle = "Gorriti"
# nombre_calle = "CRÁMER"
# nombre_calle = "corrientes"
# print(nuevo_text)


def sin_tilde(nombre_calle):
    return nombre_calle.translate(str.maketrans("ÁÉÍÓÚ", "AEIOU"))


def calle_txt(nombre_calle=None):
    file_txt = ruta
    calle_info = []

    print(nombre_calle)
    nombre_calle = (' ').join(nombre_calle.split('_'))
    print('Despues Split y Strip', nombre_calle.strip())
    nombre_calle = f'{nombre_calle.upper()}'
    print("Despues de (calle)", nombre_calle)
    nombre_calle = sin_tilde(nombre_calle)
    print("Sin tilde", nombre_calle)

    pattern = re.compile(r"({0} \(calle\)|{0} \(avenida\))".format(nombre_calle))

    #(CRAMER \(calle\)|CRAMER \(avenida\))
    with open(file_txt, encoding='latin1') as openfile:
        for linea in openfile:

            if pattern.search(linea) is not None:
                #print(linea)
                calle_info.append(linea)

    if calle_info:
        return calle_info[0]
    print(calle_info)
    return calle_info


# print(calle_txt(nombre_calle))
