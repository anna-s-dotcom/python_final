import pickle

import sys

sys.path.insert(1, 'C:/Python/GK/Codes/Tag09')

import dozent_projekt1



# with open('pkl.pickle', 'rb') as file:
#     lis = pickle.load(file)
#     print(lis)
#     for i in range(6):
#         try:
#             lis = pickle.load(file)
#             print(lis)
#         except:
#             print('No more Data!')

# # ohne 'with' operator
# file = open('pkl.pickle', 'rb')
# lis = pickle.load(file)
# file.close()

############## Lehrer:



import pickle
import sys
sys.path.append('C:/Python/GK/Codes/Tag09')
import dozent_projekt1

file = open('../lehrer.pickle', 'rb')
lehrer = pickle.load(file)
file.close()

print(lehrer.name)
