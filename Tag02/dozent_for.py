# l = [5, 4, 6, 7, 8]
#
# for i in l:
#     print(i)
#     print('hello')
#
# print('end')

# l = []
# for i in range(3):
#     x = input('Buchstabe eingeben: ')
#     l.append(x)
#
# print(l)

# l = [5, 4, 6, 7, 8]
#
# for i in range(1, 5):
#     print(l[i])
#
# for i in range(1, 10, 2):
#     print(i)

for i in range(10, -1, -1):
    print(i)

# wird über den zugriffsoperator liste[x] auf eine liste zugegriffen,
# verändert man das element der liste an der stelle x
l = [5, 4, 6, 7, 8]
for i in range(len(l)):
    l[i] = 1
print(l)
print(i)
print()

# i nimmt wert des elements der liste an, aber ist unabhängig von ihr
# verändern von i hat keinen einfluss auf die liste
print("ohne l[i]")
l = [5, 4, 6, 7, 8]
for i in l:
    i = 1
print(l)
print(i)
print()
