# Aufgabe 5)
# Lies einen beliebigen Satz als String ein.
# 1) Gib die Anzahl der Zeichen im String wieder.


satz = 'Dies ist ein Satz.'
# satz = input('Lies Satz ein: ')
print(len(satz))

# 2) Überprüfe ob das letzte Zeichen ein Satzzeichen ist. (. ! ?)

['.', '!', '?'] in last = satz[-1]

print(last)


# 3) Überprüfe ob das erste Zeichen Großgeschrieben ist. (Stringmethode: isupper())

first = satz[0].isupper()
first = satz[0] == satz[0].upper()

print(first)
# 4) Gib die Anzahl der Wörter im Satz wieder.

print(len(satz.split()))

counter = 0
for c in satz:
    if c == ' ':
        counter += 1

words = counter+1
print(words)
