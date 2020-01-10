mail = input("Emailadresse eingeben: ")

# mail = "bla@a.com"

# 1
if "@" in mail and "." in mail:
    print("@ und . enthalten!")
else:
    print("Kein @ oder . enthalten!")
print()

# 2
at = 0
dot = 0
for i in range(len(mail)):
    if mail[i] == "@":
        at = i
    if mail[i] == ".":
        dot = i
if at < dot:
    print("@ kommt vor .")
else:
    print("@ kommt nicht vor .")
print()



















# 3
at = 0
dot = 0
for i in range(len(mail)):
    if mail[i] == "@":
        at = i
    if mail[i] == ".":
        dot = i
if dot - at == 1:
    print("Die Zeichen liegen direkt hintereinander.")
else:
    print("Die Zeichen liegen nicht direkt hintereinander.")

# 4
if mail[0] != "@" and mail[-1] != ".":
    print("Korrekte Eingabe")
else:
    print("Falsche Eingabe")
print()

# 5
at = 0
dot = 0
for i in range(len(mail)):
    if mail[i] == "@":
        at = i
    if mail[i] == ".":
        dot = i
# int 0 wird als False interpretiert
if dot and at and at < dot and at - dot != 1 and mail[0] != "@" and mail[
        -1] != ".":
    print("Es handelt sich um eine Emailadresse.")
else:
    print("Es handelt sich nicht um eine Emailadresse!")
print()
