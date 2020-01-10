path = '../../Data/'
with open(path+'maxresdefault.jpg', 'rb') as file:
    bits = file.read()

# print(bits)

# with open('dog.jpg', 'wb') as data:
#     data.write(bits)

# ohne with:

data = open('dog.jpg', 'wb')
data.write(bits)
data.close()
