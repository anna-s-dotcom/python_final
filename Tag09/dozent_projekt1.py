class Schulklasse:
    def __init__(self, stufe, lehrer, schueler):
        self.stufe = stufe
        self.lehrer = lehrer
        self.schueler = schueler
        self.schueler_anzahl = self.anz()

    # 1)
    def anz(self):
        return len(self.schueler)

    def stufen_test(self):
        test = True
        if self.stufe == self.lehrer.stufe:
            for s in self.schueler:
                if self.stufe != s.stufe:
                    test = False
                    break

        if self.stufe != self.lehrer.stufe:
            test = False

        return test


    def durchschnitt(self):
        d = 0
        for s in self.schueler:
            d += s.durchschnitt()

        return d/len(self.schueler)


    def __str__(self):
        return f"Lehrer: {self.lehrer}, Stufe: {self.stufe}"

class Klassenlehrer:
    def __init__(self, name, stufe, gehalt):
        self.name = name
        self.stufe = stufe
        self.gehalt = gehalt


class Schueler:
    def __init__(self, name, stufe, noten = []):
        self.name = name
        self.stufe = stufe
        self.noten = noten.copy()

    def get_grades(self, anz):
        import random

        for i in range(anz):
            self.noten.append(random.randint(1, 6))

    def durchschnitt(self):
        if len(self.noten) > 0:
            return sum(self.noten)/len(self.noten)
        else:
            return 0


    def __str__(self):
        return f"Name: {self.name}, Noten: {self.noten}"
#
sch = ['heinz', 'erich', 'lisa', 'heidrun']
#
# l = 'meyer'
#
# klasse = Schulklasse(4, l, sch)
#
# # print(klasse)
# # print(klasse.schueler)
#
schueler_list = []
for s in sch:
    schueler_list.append(Schueler(s, 4))

for schueler in schueler_list:
    schueler.get_grades(5)
    print(schueler, 'Durchschnitt:', schueler.durchschnitt())

for i in range(len(schueler_list)):
    schueler_list[i].get_grades(5)

schueler_list[0].noten = [1,5,6]
schueler_list[1].noten = [2,4,4]
schueler_list[2].get_grades(4)
schueler_list[3].get_grades(4)

for schueler in schueler_list:
    print(schueler.noten)
print(schueler_list)
l = Klassenlehrer('meyer', 4, 2800)
klasse = Schulklasse(4, l, schueler_list)

print(klasse.stufen_test())
print(klasse.durchschnitt())
