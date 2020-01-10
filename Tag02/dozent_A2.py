# Erstelle ein Programm, welches vom Benutzer einen Wochentag einliest.
# (als Mo, Di, Mi, Do, Fr)

# Die Ausgabe soll: "Sie haben Montag gewählt." sein für Mo.
# Nutze ein Dictionary.

days = {"Mo": "Montag",
        "Di": "Dienstag",
        "Mi": "Mittwoch",
        "Do": "Donnerstag",
        "Fr": "Freitag"}

day = input("Tag eingeben (Mo - Fr): ")
# falls input == montag -> Mo
day = days[day[:2].capitalize()]

print(f"Sie haben {day} gewählt.")
