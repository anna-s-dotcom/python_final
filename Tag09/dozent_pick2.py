import pickle

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

file = open('lehrer.pickle', 'rb')
lehrer = pickle.load(file)
file.close()

print(lehrer)
