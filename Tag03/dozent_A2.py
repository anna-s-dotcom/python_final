import random

# erstellt eine zahl zwichen 1 und 5 (incl 1 und 5)
# print(random.randint(1, 5))

# Erstelle eine Funktion, welche den Abstand
# zwischen zwei Zahlen ermittelt.
# Der Abstand ist die differenz der zwei Zahlen, aber immer positiv.

# Berechne den Abstand zwischen zwei zufälligen Zahlen.

# Bonus: Berechne zehn Abstände zwischen je zwei zufälligen Zahlen.

x = random.randint(1, 10)
y = random.randint(1, 10)

def my_betrag1(a, b):
    if a >= b:
        return a - b
    else:
        return my_betrag1(b, a)

def my_betrag2(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def my_betrag3(a, b):
    c = a-b
    if c > 0:
        return c
    return -c

def my_betrag4(a, b):
    return abs(a-b)

print(x, y)
e1 = my_betrag1(x, y)
print(e1)
e2 = my_betrag2(x, y)
print(e2)
e3 = my_betrag3(x, y)
print(e3)
e4 = my_betrag4(x, y)
print(e4)

for i in range(10):
    print(my_betrag1(random.randint(1,10), random.randint(1,10)))

def betragX10():
    for i in range(10):
        print(my_betrag1(random.randint(1,10), random.randint(1,10)))

print()

betragX10()
