import io


# ./calles_text.txt
def text_to_list():
    file_txt = 'calles_text.txt'
    nuevo_text = []
    nuevo_p = []
    with io.open(file_txt) as openfile:
        for line in openfile:
            nuevo_text.append(line.rstrip('\n'))
    return nuevo_text
