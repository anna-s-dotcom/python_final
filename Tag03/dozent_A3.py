
x = 9

quadX = x**2
print(quadX)
sqrtX = x**0.5
print(sqrtX)

# Berechne im mehrdimensionalen Raum den Abstand zwischen zwei Punkten.

# für [x1, y1], [x2, y2] = ((x1-x2)**2 + (y1 - y2)**2)**0.5

def abstand(a, b):
    qsum = 0
    for i in range(len(a)):
        qsum += (a[i]-b[i])**2
    return qsum**0.5

x = [0, 0]
y = [1, 1]

print(abstand(x, y))
