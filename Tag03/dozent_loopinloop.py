# for i in range(3):
#     print('outer loop', i)
#     for j in range(3):
#         print('inner loop', j)
#
#     print('end inner loop')
#
# print('end')


# Ausgabe:
# Zeile 0: 0 1 2
# Zeile 1: 0 1 2
# ...
# Zeile n: 0 1 2


#äußere schleife == anz der zeilen
for i in range(10):
    print(f"Zeile {i}: ", end= "")
    # noch kein Break
    for j in range(3):
        print(j, end = "")
    print()
