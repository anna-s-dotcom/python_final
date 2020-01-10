class Fahrzeug:
    def __init__(self, x, y = 'blau'):
        self.geschwindigkeit = x
        self.pub = 'public'
        self._prot = 'protected'
        self.__priv = 'private'
        self.colour = self.set_colour()

    def set_colour(self):
        self.colour = 'rot'
        return self.colour

    def beschleunigen(self, x):
        'Beschleunigt um x'
        # kommentar
        self.geschwindigkeit += x

    def __str__(self):
        return f'Fahrzeuggeschwindigkeit: {self.geschwindigkeit}'


if __name__ == '__main__':

    auto = Fahrzeug(45)
    # auto.set_colour()
    print(auto.colour)

    auto.bla = 'bla bla'
    print(auto.bla)

    print(auto.geschwindigkeit)

    lkw = Fahrzeug(80, 'grün')
    print(lkw.colour)

    print(lkw.geschwindigkeit)

    auto.beschleunigen(90)

    print(auto.geschwindigkeit)
    print(lkw.geschwindigkeit)

    print(auto)
    print(lkw)
