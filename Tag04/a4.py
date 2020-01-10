# 1
# mit Übergabe der Zahlen als Liste
def kllistZahl(l):
    kl = l[0]  # erstes Element der Liste als kleinste Zahl setzen
    for i in l:
        if i < kl:
            # wenn das Element i in der liste kleiner ist, als unsere kleinste Zahl -> Überschreiben
            kl = i
    return kl

print(kllistZahl([5, 6, 8, 1, 4]))
print()


# 2
def grzehn(l):
    gr = l[0]  # erstes Element der Liste als größte Zahl setzen
    for i in l:
        if i > gr:
            # wenn das Element i in der liste größer ist, als unsere größte Zahl -> Überschreiben
            gr = i
    return gr > 10


print(grzehn([5, 6, 8, 1, 4]))
print(grzehn([5, 6, 8, 1, 4, 11]))
print()
print()


# 3
def klnull(l):
    kl = l[0]  # erstes Element der Liste als kleinste Zahl setzen
    for i in l:
        if i < kl:
            # wenn das Element i in der liste kleiner ist, als unsere kleinste Zahl -> Überschreiben
            kl = i
    return kl < 0


print(klnull([5, 6, 8, 1, 4, -1]))
print(klnull([5, 6, 8, 1, 4]))
print()
print()

# 4
def hilfsfunc(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(-10, 20))
    return l

print(hilfsfunc(10))

# mit list comprehension
def hilfsfunc2(n):
    import random
    return [random.randint(-10, 20) for i in range(n)]

print(hilfsfunc2(10))
