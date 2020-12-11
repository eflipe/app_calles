import re
import os

file_txt = 'calles_text_list.txt'

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
ruta = os.path.join(basedir, file_txt)
print(ruta)


def sin_tilde(nombre_calle):
    return nombre_calle.translate(str.maketrans("ÁÉÍÓÚ", "AEIOU"))


def search_calle(nombre_calle=None):
    file_txt = ruta
    calle_info = []

    print(nombre_calle)
    nombre_calle = (' ').join(nombre_calle.split('_'))
    # print('Despues Split', nombre_calle)
    nombre_calle = f'{nombre_calle.upper()}'
    # print("Despues de (calle)", nombre_calle)
    nombre_calle_sin_tilde = sin_tilde(nombre_calle)
    # print("Sin tilde", nombre_calle)

    pattern = re.compile(r"({0}|{1} \(calle\)|{0}|{1} \(avenida\))".format(nombre_calle, nombre_calle_sin_tilde))

    #(CRAMER \(calle\)|CRAMER \(avenida\))
    with open(file_txt, encoding='latin1') as openfile:
        index_1 = 0
        index_2 = 0

        for linea in openfile:

            if pattern.search(linea) is not None:
                index_1 = 1
                #print("Si, index_1")
                #print(linea)
                continue
                # print(linea)

            if index_1 == 1:
                if nombre_calle.lower().title() in linea:
                    linea = linea.replace('- ', '')
                    linea = linea.replace('', '"').replace('', '"')
                    calle_info.append(linea.strip())
                    break


    if calle_info:
        # print("INFO CALLE", calle_info)
        return calle_info[0]

    return calle_info
