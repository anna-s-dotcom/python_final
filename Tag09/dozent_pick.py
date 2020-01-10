import pickle
import dozent_projekt1
# from dozent_projekt1 import Klassenlehrer

# for i in range(5):
#     data = open('pkl.pickle', 'ab')
#     pickle.dump(i, data)
#     data.close()


# Klassenlehrer(name, stufe, gehalt)
lehrer = dozent_projekt1.Klassenlehrer('Schmitt', 8, 2900)

file = open('lehrer.pickle', 'wb')
pickle.dump(lehrer, file)
file.close()
