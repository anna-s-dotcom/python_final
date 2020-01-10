# 1) Erstelle ein Programm welches eine Textdatei erstellt,
# die folgendermaßen aussieht:
#
# 1. Zeile
# 2. Zeile
# 3. Zeile
# 4. Zeile
# ...
# 10. Zeile

s = ''
for i in range(1, 11):
    s += f"{i}. Zeile\n"

file = open('a1.txt', 'w')
file.write(s)
file.close()

file = open('a1_2.txt', 'w')
for i in range(1, 11):
    file.write(f"{i}. Zeile\n")
file.close()


# bei mehrmaliger ausführung wird die datei immer größer

for i in range(1, 11):
    file = open('a1_3.txt', 'a')
    file.write(f"{i}. Zeile\n")
    file.close()

# 2) Erstelle ein Programm, welches die ungeraden Zeilen ausliest und ausgibt.

file = open('a1.txt')
text = file.readlines()
file.close()

for i in range(0, 10, 2):
    print(text[i], end= "")
