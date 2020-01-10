# import:
# alle funktionen von random!
import random
# aufruf mit modul.funktion()
r1 = random.randint(1, 10)
# nur randint und random werden importiert
from random import randint, random
# aufruf über funktion
r2 = randint(1, 10)
# alle funktionen von random werden importiert
from random import *
# aufruf über funktion()
r3 = randint(1, 10)
# alias geben:
import random as rd
# aufruf: alias.funktion()
r4 = rd.randint(1, 10)
# funktion alias geben
from random import randint as ri
# aufruf über alias
r5 = ri(1, 10)

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
