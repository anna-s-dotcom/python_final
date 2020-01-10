# Schreibe ein Programm, welches den User auffordert einen Geldbetrag einzugeben.
# Gib dem Automaten bescheid, wieviele Scheine er ausgeben soll.

# Bei Zahl 85:
# 0 x 200
# 0 x 100
# 1 x 50
# 1 x 20
# 1 x 10
# 1 x 5

# Funktionen: input(), Modulo: %, Ganzzahlige Division: //

betrag = int(input('Betrag eingeben: '))

print(f"{betrag // 200} x 200")
betrag = betrag % 200

print(f"{betrag // 100} x 100")
betrag = betrag % 100

print(f"{betrag // 50} x 50")
betrag = betrag % 50

print(f"{betrag // 20} x 20")
betrag = betrag % 20

print(f"{betrag // 10} x 10")
betrag = betrag % 10

print(f"{betrag // 5} x 5")
betrag = betrag % 5
