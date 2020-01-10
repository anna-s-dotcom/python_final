# 1
x = int(input("Zahl 1: "))
y = int(input("Zahl 2: "))

l = list(range(x, y + 1))
# oder:
l = []
for i in range(x, y + 1):
    l.append(i)
    
# 2
for i in l:
    print(i)
print()

# 3
for i in l:
    print(i, end=" ")
print()

# 4
for i in l:
    if i % 2 == 0:
        print(i)
print()

# da int 0 == False geht auch:
for i in l:
    if not i % 2:
        print(i)
print()

# 5
for i in l:
    if i % 2 == 1:
        print(i)
print()

# da int 0 == False geht auch:
for i in l:
    if i % 2:
        print(i)
print()
