
# try:
#     file = open("Textdokument.txt")
#     text = file.read()
#
#     print(text)
#
# except:
#     print('File not found!')


import os.path
import pathlib
import sys

p = pathlib.Path('.')

# print(p.absolute())
# print(os.path.abspath('.'))
# print(sys.path[0])
# print()
#
# for i in p.iterdir():
#     print(i)
#     print(i.is_dir())
#     print(i.is_file())
#     print(os.path.isdir(i))
#     print(os.path.isfile(i))
#

# file = open('test.txt', 'w')
# text = input('Text eingeben: ')
# file.write(text)
# file.close()


# file = open('test.txt', 'a')
# text = input('Text eingeben: ')
# file.write(text)
# file.write("\n")
# file.close()


# file = open('Projekttag 1 Aufgaben.pdf', 'rb')
# text = file.read()
# file.close()
# print(text)
#

# # absoluter pfad
# file = open("C:/Python/GK/Data/test.txt")
# # relative pfad
# file = open("../../Data/test.txt")
# text = file.read()
# file.close()
# print(text)
#
#
# # # Kopieren einer Datei:
# file = open('Projekttag 1 Aufgaben.pdf', 'rb')
# text = file.read()
# file.close()
#
# file = open("./Neuer Ordner/copy2.pdf", 'wb')
# file.write(text)
# file.close()


file = open('test.txt', 'r')

text = file.readlines()
print(text)
print(file.tell())

file.seek(0)
text = file.read()
print("Text:", text)
