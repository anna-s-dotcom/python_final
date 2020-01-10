s = input("Gib 'Hello World!' ein: ")

test = "Hello World!"

# 1
if s == test:
    print("Korrekte Eingabe")
else:
    print("Falsche Eingabe")
print()

# 2
if s.upper() == test.upper():
    print("Korrekte Eingabe")
else:
    print("Falsche Eingabe")
print()

# geht auch:
if s.lower() == test.lower():
    print("Korrekte Eingabe")
else:
    print("Falsche Eingabe")
print()

# 3
def hwtest(eingabe):
    if eingabe == "Hello World!":
        return True
    else:
        return False

# mit eingabe in der funktion:
def hwtest2():
    eingabe = input("Gib 'Hello World!' ein: ")
    if eingabe == "Hello World!":
        return True
    else:
        return False

print()
print(hwtest(s))

# 4
def hwtest2():
    while True:
        eingabe = input("Gib 'Hello World!' ein: ")
        if eingabe == "Hello World!":
            print('Korrekte Eingabe!')
            break
        print("Falsche Eingabe!")

print()
hwtest2()
