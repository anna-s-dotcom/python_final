mail = 'mail@bla.com'
# mail = input('Mail eingeben: ')

# Aufgabe 3)
# Lies einen String ein und Überprüfe ob der String eine Email-Adresse ist. (xxx@xxx.xxx)
# Natürlich nicht real, sondern mit den folgenden Abfragen:
# 1) Überprüfe ob „@“ und „.“ enthalten sind.

def at_dot_in(mail):
    if '@' in mail and '.' in mail:
        return True
    else:
        return False

def at_dot_in2(mail):
    at = False
    dot = False
    for c in mail:
        if c == "@":
            at = True
        if c == '.':
            dot = True
    return at and dot

print(at_dot_in(mail))
print(at_dot_in2(mail))


# 2) Überprüfe ob ein „.“ nach dem „@“ vorkommt.
def at_before_dot(mail):
    at = 0
    dot = 0
    for i in range(len(mail)):
        if mail[i] == "@":
            at = i
        if mail[i] == ".":
            dot = i
    if at < dot:
        return True
    else:
        return False

print(at_before_dot(mail))
# 3) Überprüfe ob mindestens ein Zeichen zwischen dem „@“ und dem „.“ liegt.

def between_at_dot(mail):
    at = 0
    dot = 0
    for i in range(len(mail)):
        if mail[i] == "@":
            at = i
        if mail[i] == ".":
            dot = i
    return (at - dot) > 1

# 4) Überprüfe ob das erste Zeichen kein „@“ und das letzte Zeichen kein „.“ ist.

def first_last(mail):
    return mail[0] != '@' and mail[-1] != '.'

print(first_last(mail))

# 5) Kombiniere die obigen Überprüfungen, wenn alle zutreffen, dann handelt es sich um eine Email-Adresse.

def is_mail(mail):
    if at_dot_in(mail) and at_before_dot(mail) and between_at_dot(mail) and first_last(mail):
        print('Es ist eine Mailadresse!')
    else:
        print('Es ist keine Mailadresse!')
