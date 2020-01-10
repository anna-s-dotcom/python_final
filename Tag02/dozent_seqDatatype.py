########### listen ###########


# zuweisung einer liste
first_list = [1, 2.4, "Hallo"]

# ausgabe ganze liste
print(first_list)

# zugriff auf einzelne elemente
# print(first_list[0])
# print(first_list[1])
# print(first_list[2])
# print(first_list[-1])
#
# # len(liste) gibt die anzahl der objekte in der liste wieder
# length = len(first_list)
# print("Länge:", length)
#
# # element an liste anhängen
# first_list.append(True)
#
# print(first_list)

# sec_list = ["dsfljö", 54, False]
#
# # concatination von listen mit +
# concat_list = first_list + sec_list
# print(concat_list)
#
# sec_list.pop(-2)
# print(sec_list)
# print()
# print(first_list)
# last = first_list.pop()
# print(first_list)
# print(last)
# first_list[1] = 54
# #### ersetzt Element, nicht neue einfügen
# print(first_list)
# # ACHTUNG! Index muss < len(liste) sein
# # print(first_list[4])


########### tupel ###########
# #
# first_tup = (1, 45, "asdf")
# print()
# print("Tupel")
# print()
# print(first_tup)
# print(first_tup[1])
# print(first_tup[-1])
# print('Länge:', len(first_tup))
# print(type(first_tup))
#
########### string ###########

s = "hellO worLd    "
print()
print('Strings')
print()
print(s[-1])

#### -1 funktioniert nicht bei Strings

# erster Buchstabe groß, alle anderen klein
print(s.capitalize())
print(s.upper())
print(s.lower())
s_split = s.split()
print(s)
print(s_split)
print(len(s))
s = s.strip()
print(len(s))

print()
print('Slicing: ')
print()
s = "hellO worLd!!!"
print("Länge", len(s))
print("Slice 6:11:", s[6:11])
print("Slice from 6:", s[6:])
print("Slice till index 10:", s[:11])

print("Slice till index 10:", s[1])
