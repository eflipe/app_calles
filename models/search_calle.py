#from open_calle import text_to_list
#from utils.open_calle import text_to_list
import io
import os

file_txt = 'calles_text.txt'

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
ruta = os.path.join(basedir, file_txt)
print(ruta)


def text_to_list():
    file_txt = ruta
    nuevo_text = []

    with open(file_txt, encoding='latin1') as openfile:
        for line in openfile:
            nuevo_text.append(line.rstrip('\n'))
#    print(nuevo_text)
    return nuevo_text

# nombre_calle = "Agüero"
#print(nuevo_text)


def calle_txt(nombre_calle=None):
    nuevo_text = text_to_list()
    nuevo_nuevo = []
    index_1 = 0
    start = 0

    for item in nuevo_text:

        if not item:
            # print("Item", item)
            index_1 = nuevo_text.index(item, start+1)
            # start = index_1
            # print('Start', start)
            # print(index_1)

        if start < index_1:
            join_text = ' '.join(nuevo_text[start:index_1])
            nuevo_nuevo.append(join_text.strip())

        start = index_1

    # print(nuevo_text)
    #print(nuevo_nuevo)

    calle_info = []
    print(nombre_calle)
    nombre_calle = (' ').joint(nombre_calle.split('_'))
    for linea in nuevo_nuevo:
        index = 0
        prev = 0

        while index < len(linea):
            linea = linea
            index = linea.find(nombre_calle, index)

            if index == -1:
                break
            print(" " * (index - prev) + f"{nombre_calle}", end='')

            prev = index + len(nombre_calle)
            index += len(nombre_calle)
            calle_info.append(linea)

        #print('\n' + linea))
    print(calle_info)
    return calle_info

#calle_txt(nombre_calle)


#     for line in openfile:
#         for part in line.strip().split('\n'):
#             print('Linea', part)
#             if part != '\n' or part != ' ':
#                 nuevo_text.append(part)
#
# print(nuevo_text)
# print((' ').join(nuevo_text))

    #linea_strip = [line.strip() for line in openfile]


        # for descripcion in line.strip().split('\n'):
        #     print('Linea:', descripcion)
        #     if nombre_calle in descripcion:
        #         print('Nombre', descripcion)
    #print(('').join(linea_strip))
