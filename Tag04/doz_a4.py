# Aufgabe 4)
# Schreibe eine Funktion, die eine beliebige Anzahl an Zahlen als Liste übergeben bekommt.
l1 =  [1, 5, 5, 4, 41, 3]
l2 =  [6, 5, 5, 4, -2, 3]
# 1) Die Funktion soll die kleinste der Zahlen ausgeben.

x = min(l1)

def my_min(lis):
    min = lis[0]
    for x in lis:
        if min > x:
            min = x
    return min

print(my_min(l1))
print(my_min(l2))

# 2) Die Funktion soll zurückgeben, ob die größte Zahl größer als 10 ist.

def gr_10(lis):
    return max(lis) > 10

print(gr_10(l1))
print(gr_10(l2))

# 3) Die Funktion soll zurückgeben, ob die kleinste Zahl kleiner als 0 ist.

def kl_0(lis):
    return min(lis) < 0

print(kl_0(l1))
print(kl_0(l2))

# 4) Schreibe eine Hilfsfunktion, welche eine Liste aus Zufallszahlen zwischen -10 und 20 erstellt.
# Die Anzahl der Zahlen soll übergeben werden.

import random

def create_list(n):
    lis = []
    for i in range(n):
        lis.append(random.randint(-10, 20))
    return lis

l = create_list(10)
print(l)
