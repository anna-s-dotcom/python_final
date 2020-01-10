# Aufgabe 8)
# Überprüfe ob ein Jahr ein Schaltjahr ist.

# 400 = True
# 100 = False
# 4 = True

def ly(y):
    return (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)

print(ly(2000))
print(ly(2004))
print(ly(2001))
print(ly(2100))

def ly_ifelse(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

print(ly_ifelse(2000))
print(ly_ifelse(2004))
print(ly_ifelse(2001))
print(ly_ifelse(2100))
