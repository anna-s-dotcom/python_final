jahr = int(input("Bitte geben Sie ein Jahr ein:"))

if jahr%400 ==0 or (jahr%4 ==0 and jahr%100!=0):
    print("Das Jahr " + str(jahr) + " ist ein Schaltjahr.")
else:
    print("Das Jahr " + str(jahr) + " ist kein Schaltjahr.")
