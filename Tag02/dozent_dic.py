l = [1,2]

# dictionary = {key:value, key:value}
d = {'hello': 'Hello World!', 10: l, True: 12, 10:'zehn'}

# aufruf über key
# print(d['hello'])
# print(d[10])
# print(d[True])
#
# print(d)
#
#
# # zuweisung/ neues element
# d['hello'] = 564.4
# d[2.5] = 'HelloW.'
#
# print(d)
#
# entfernen via key (gibt value zu key zurück)
x = d.pop(True)
print(x)
print(d)

# help(d)
x = 5
d = {'a': 1+x, 'b': 2+x}



print(d['a'])
