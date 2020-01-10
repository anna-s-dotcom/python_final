# Aufgabe 1)
# Lies zwei ganze Zahlen ein.
# 1) Erstelle eine Liste mit allen Zahlen die zwischen diesen Zahlen liegen. (Inklusive der eingelesenen Zahlen.)
a = int(input('Zahl 1: '))
b = input('Zahl 2: ')
b = int(b)

li = list(range(a, b + 1))

li = []
for i in range(a, b+1):
    li.append(i)


# 2) Gib alle Zahlen untereinander aus.
for i in li:
    print(i)

# 3) Gib alle Zahlen hintereinander aus.
for i in li:
    print(i, end = ' ')

# 4) Gib nur die geraden Zahlen aus.

for i in li:
    if i%2 == 0:
        print(i)

# 5) Gib nur die ungeraden Zahlen aus.

for i in li:
    if i%2:
        print(i)
