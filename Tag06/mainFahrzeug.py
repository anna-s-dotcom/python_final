from module.fahrzeug import Fahrzeug

# die datei liegt im ordner 'module' (welcher auf der gleichen ebene wie die ausführende Datei liegt)

auto = Fahrzeug(100)
auto.beschleunigen(-20)

# print(auto)
#
# print(dir(Fahrzeug))

#
    # def __init__()
    #     self.pub = 'public'
    #     self.__priv = 'private'
    #     self._prot = 'protected'

print(auto.pub)
print(auto._prot)
# print(auto.__priv)
auto._Fahrzeug__priv = 'not so private'
print(auto._Fahrzeug__priv)
