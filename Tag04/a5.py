satz = input("Satz eingeben: ")

# 1
print(len(satz))

# 2
if len(satz) > 0:
    if satz[-1] in [".", "!", "?"]:
        print("Das letzte Zeichen ist ein Satzzeichen.")
    else:
        print("Das letzte Zeichen ist kein Satzzeichen.")

# 3
if len(satz) > 0:
    if satz[0] == satz[0].upper():
        print("Das erste Zeichen ist groß geschrieben.")
    else:
        print("Das erste Zeichen ist nicht groß geschrieben.")

# 4
print(len(satz.split()))
