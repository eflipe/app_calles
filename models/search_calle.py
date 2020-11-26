#from open_calle import text_to_list
#from utils.open_calle import text_to_list
import io, os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
global file_txt
file_txt = os.path.join(PARENT_DIR, 'calles_text.txt')


def text_to_list():
    #file_txt = file_txt
    nuevo_text = []

    with io.open(file_txt) as openfile:
        for line in openfile:
            nuevo_text.append(line.rstrip('\n'))
#    print(nuevo_text)
    return nuevo_text

#print(nuevo_text)

nombre_calle = "Moldes"

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

calle_txt(nombre_calle)


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
