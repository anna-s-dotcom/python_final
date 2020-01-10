print("Hello World!")

# mit """...""" kann man strings über mehrere zeilen ausgeben
print(f"""6 + 5
{6 + 5}""")
print()

print("6 - 5\n" + str(6 - 5))
print()

# alles was in format() steht wird berechnet und anstelle von {} ausgegeben
print("6 * 5: {}".format(6 * 5))
print()

# f"..." alle Werte in {} werden berechnet und ausgegeben
print(f"6 / 5: {6 / 5}")
print()

# zwei strings werden konkatiniert (zusammengefügt)
print("11 % 2: " + str(11 % 2))
print()

# ausgabe von zwei werten, string und berechnung
print("11 // 2:", 11 // 2)
print()

# boolsche ausdrücke
print('Boolean:')
print(11 < 10)
print(11 > 10)
print(11 <= 11)
print(11 >= 11)
# boolsche gleich: ==, da = ein zuweisungsoperator ist
print(23 == 23.0)
# != ungleich
print(23 != 23)
print(True == True)

# None ist der leere Wert
x = None
print(type(x))

x = 7
# str(x) gibt einen string zurück mit wert "x"
x = str(x)
print(type(x))

x = int("45")
print(type(x))
