import random

# 1
def createMat(a, b):
    matrix = []
    for i in range(a):
        row = []
        for j in range(b):
            row.append(round(random.random(), 2))
        matrix.append(row)
    return matrix

matrix = createMat(3, 5)

# 2
def printMat(m):
    for line in m:
        for x in line:
            x = str(x)
            while len(x) < 4:
                x += '0'
            print(x, end = '  ')
        print()
printMat(matrix)
print()

# 3
for i in range(1, len(matrix[0]), 2):
    print([row[i] for row in matrix])
print()

# umständlicher:
for i in range(1, len(matrix[0]), 2):
    spalte = []
    for j in range(len(matrix)):
        spalte.append(matrix[j][i])
    print(spalte)
print()

# 4
summen = []
summe = 0
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        summe += matrix[j][i]
    summen.append(summe)
    summe = 0
print(summen)
print()

# 5
summen = []
summe = 0
for i in range(len(matrix)):
    summe = sum(matrix[i])
    summen.append(summe)
    summe = 0
print(summen)
print()

# einfacher
summen = []
for row in matrix:
    summen.append(sum(row))
print(summen)
print()
