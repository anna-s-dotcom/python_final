# for i in range(4):
#     print(i)
#     break
#
# print('Ende')

# Teste ob in einer Liste mindestens eine gerade Zahl enthalten ist.
# Wenn ja, gib ja aus.

# Bonus: Wenn nein, gib nein aus.

l1 = [1, 5, 9, 7]
l2 = [5, 3, 2, 5, 8]

# Tipp: nutze den Modulo (%) Operator

# x = l1
# b = True
# for i in x:
#     if i%2 == 0:
#         print('l1 enthält gerade zahl')
#         b = False
#         break
#
# if b:
#     print('l1 enthält keine gerade zahl')
#
# x = l2
# b = True
# for i in x:
#     if i%2 == 0:
#         print('l2 enthält gerade zahl')
#         b = False
#         break
# if b:
#     print('l2 enthält keine gerade zahl')


x = l1

for i in x:
    if not i%2:
        print('enthält gerade zahl')
        break

if i%2:
    print('enthält keine gerade zahl')
