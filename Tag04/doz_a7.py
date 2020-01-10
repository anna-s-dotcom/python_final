# Aufgabe 7)
# Erstelle eine Funktion, welche eine Zahl und einen Befehl übergeben bekommt.
# Der Befehl soll „lin“ oder „quad“ sein.
# Je nach dem soll die Funktion ausgeführt werden:
# lin = 4*x+5
# quad = 4*x2+5*x+6
# 1) Nutze ein if/else Konstrukt.

def linquad(x, f = 'lin'):
    if f == 'lin':
        return 4 * x + 5
    elif f == 'quad':
        return 4 * x**2 + 5*x + 6
    else:
        print('Falsche Eingabe')

y = linquad(5, 'lin')
print(y)

y = linquad(10, 'quad')
print(y)

# 2) Nutze ein Dictionary.

def linquad_dic(x, f):
    d = {'lin': 4 * x + 5, 'quad': 4 * x**2 + 5*x + 6}
    return d[f]

y = linquad_dic(5, 'lin')
print(y)

y = linquad_dic(10, 'quad')
print(y)

# wichtig, wenn d erstellt wird werden die werte ausgerechnet!
print()
x = 5
d = {'lin': 4 * x + 5, 'quad': 4 * x**2 + 5*x + 6}
print(d['lin'])
# neu wählen von x hat keine auswirkung mehr auf d
x = 10
print(d['lin'])

def f1():
    print('F1')

def f2(x):
    return 4 * x

# wenn funktion als value, dann ohne ()
# - wenn die funktion nicht direkt aufgerufen werden soll
d2 = {'f_1': f1, 'f_2': f2}
d2['f_1']()

y = d2['f_2'](5)

print(y)
