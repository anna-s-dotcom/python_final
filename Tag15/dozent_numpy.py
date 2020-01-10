import numpy as np

lis = [1, 5, 8, 4, 7, 3]
for i in range(len(lis)):
    lis[i] += 3
print(lis)

lis = [1, 5, 8, 4, 7, 3]
lis2 = []
for i in lis:
    lis2.append(i+3)
print(lis2)

lis = [1, 5, 8, 4, 7, 3]
lis = [i+3 for i in lis]
print(lis)

arr = np.array([1, 5, 8, 4, 7, 3])
print(arr)
arr = arr + 3
print(arr)
print(type(arr))

print(arr*5)
print(arr)

print(arr.mean())
print(arr.max())
print(arr.min())
