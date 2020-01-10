# Erstelle mit Hilfe einer geschachtelten Schleife die folgende Ausgabe:

# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

for i in range(4):
    for j in range(4):
        print(j+1, end = " ")
    print()
print()
for i in range(4):
    for j in range(1, 5):
        print(f" {j}", end = "")
    print()
print()

# Bonus erstelle die folgende Ausgabe:

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
print()
for i in range(4):
    for j in range(4):
        print(i+1, end = " ")
    print()
print()
for i in range(1, 5):
    for j in range(4):
        print(f" {i}", end = "")
    print()
