# Aufgabe 2)
# Lies den String „Hello World!“ ein.
# 1) Überprüfe ob die Eingabe korrekt ist.

s = input('Gib "Hello World!" ein: ')

# test = "Hello World!"
#
# if s == "Hello World!":
#     print('korrekt')
# else:
#     print('falsch')
#
#
# # 2) Überprüfe ob die Eingabe korrekt ist, wobei nicht auf Groß- und Kleinschreibung geachtet wird.
#
# if s.lower() == "Hello World!".lower():
#     print('korrekt')
# else:
#     print('falsch')
#
# # 3) Schreibe die Überprüfung der Eingabe als Funktion, welche einen Wahrheitswert zurück gibt.
#
# def test1(x):
#     if x == "Hello World!":
#         return True
#     else:
#         return False
#
# print(test1(s))

# 4) Schreibe eine Funktion, welche solange Strings einließt, bis die Eingabe korrekt ist.

def test2(s):
    while s != "Hello World!":
        print('Falsche Eingabe!')
        s = input('Gib "Hello World!" ein: ')
    print('korrekt')

test2(s)
