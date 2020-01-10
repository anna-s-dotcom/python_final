from fahrzeug2 import Fahrzeug


class Lkw(Fahrzeug):
    def __init__(self, marke, beladung):
        Fahrzeug.__init__(self, marke, 'lkw')
        # super() ist übergeordnete klasse
        # super().__init__(marke, typ = 'lkw')
        self.beladung = beladung


    def beschleunigen(self, x):
        max = 80
        if self.get_speed() + x > max:
            self.bremsen()
            super().beschleunigen(max)
        else:
            super().beschleunigen(x)

    def __str__(self):
        # return f"{self.marke}, {self.farbe}, {self.get_speed()}km/h, {self.beladung} Tonnen Beladung"
        return super().__str__() + f", {self.beladung} Tonnen Beladung"

laster = Lkw('Skoda', 5.5)
laster.beschleunigen(60)

print(laster)
laster.beschleunigen(60)
print(laster)
