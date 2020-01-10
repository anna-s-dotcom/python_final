# Aufgabe 6)
# 1) Erstelle eine Funktion, welche eine 5x5 Matrix mit zufälligen Zahlen zwischen 0 und 1 enthält,
# diese sollen zwei Nachkommastellen haben. (Mit Hilfe der Funktionen: random.random(), round())
import random

def create_mat(x, y):
    m = []
    row = []
    for i in range(x):
        for j in range(y):
            row.append(round(random.random(), 2))
        m.append(row)
        row = []
    return m
mat = create_mat(3, 5)

# print(mat)


# Alternative 1
def create_list(n):
    l = []
    for i in range(n):
        l.append(round(random.random(), 2))
    return l

def create_mat2(x, y):
    m = []
    for i in range(x):
        m.append(create_list(y))
    return m
print()
mat2 = create_mat2(3, 5)
# print(mat2)

# Alternative 2
def create_mat3(x, y):
    m = []
    for i in range(x):
        row = [round(random.random(), 2) for i in range(y)]
        m.append(row)
    return m

print()
mat3 = create_mat3(3, 5)
# print(mat3)

# 2) Erstelle eine Funktion, die eine schöne Ausgabe hat.
# z.B:
# 0.85 0.22 0.41 0.02 0.83
# 0.54 0.61 0.54 0.67 0.13
# 0.92 0.18 0.98 0.46 0.57
# 0.41 0.32 0.03 0.04 0.20
# 0.77 0.21 0.39 0.49 0.82

def printMat(m):
    for row in m:
        for elem in row:
            print(f"{elem:.2f}", end = ' ')
        print()

printMat(mat)

def printMat_join(m):
    for row in m:
        print(" ".join(str(x) for x in row))
# print()
# printMat_join(mat)

# 3) Gib jede gerade Spalte als Liste aus.

col = []
for j in range(1, len(mat[0]), 2):
    for i in range(len(mat)):
        col.append(mat[i][j])
    # print(col)
    col = []

# 4) Summiere alle Elemente einer Spalte und gib die Summen als Liste aus.
sums = []
col_sum = 0

for col in range(len(mat[0])):
    for row in range(len(mat)):
        col_sum += mat[row][col]
    sums.append(col_sum)
    col_sum = 0

print(sums)
# 5) Summiere alle Elemente einer Zeile und gib die Summen als Liste aus.

sums = []
for row in mat:
    sums.append(sum(row))

sums2 = [sum(row) for row in mat]

# print(sums)
# print(sums2)
