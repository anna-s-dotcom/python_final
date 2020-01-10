# Lies seperat einen Vor- und Nachnamen ein.
# Bilde daraus den Satz: "Ich heiße Max Mustermann."
# (Für Vorname = 'Max', Nachname = 'Mustermann')

name = input('Vornamen eingeben: ')
surname = input('Nachnamen eingeben: ')

print(f"Ich heiße {name} {surname}.")
print("Ich heiße", name, surname, end=".\n")
print("Ich heiße " + name + " " + surname + ".")

# help(print)
