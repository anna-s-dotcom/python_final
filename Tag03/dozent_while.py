i = 0
while i < 10:
    i += 1
    # i = i + 1
    print(i)

# Aufgabe: Erstelle ein Programm, welches abfragt, ob ein bestimmter
# Prozess wiederholt werden soll.
# Wenn 'y', dann wiederhole die Abfrage, wenn 'n', dann nicht.

# 'Möchten sie den Prozess wiederholen? y/n'

# Bonus: Fange eine falsche Eingabe ab. (Und wiederhole den Vorgang.)
# 'Falsche Eingabe!'

i = 'y'

while i != 'n':
    i = input('Möchten sie den Prozess wiederholen? y/n ')
    # if i != 'y' and i != 'n':
    #     print('Falsche Eingabe!')
    # if not (i == 'y' or i == 'n'):
    #     print('Falsche Eingabe!')
    if i not in ['y', 'n']:
        print('Falsche Eingabe!')
