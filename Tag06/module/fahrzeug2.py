from random import choice


class Fahrzeug:
    def __init__(self, marke, typ):
        self.marke = marke
        self.typ = typ
        self.farbe = choice(['rot', 'silber', 'schwarz'])
        self.__geschwindigkeit = 0

    def beschleunigen(self, x):
        max = 130
        if self.__geschwindigkeit + x < max:
            self.__geschwindigkeit += x
        else:
            self.__geschwindigkeit = max

    def bremsen(self):
        self.__geschwindigkeit = 0

    def get_speed(self):
        return self.__geschwindigkeit

    def __str__(self):
        return f"{self.marke}, {self.farbe}, {self.get_speed()}km/h"

# pkw = Fahrzeug('Benz', 'PKW')
# lkw = Fahrzeug('Lada', 'LKW')
#
# print(pkw)
# print(lkw)
#
# pkw.beschleunigen(90)
# print(pkw)
# pkw.beschleunigen(90)
# print(pkw)
# pkw.bremsen()
# print(pkw)
