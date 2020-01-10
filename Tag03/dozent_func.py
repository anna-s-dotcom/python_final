def plus5(x):
    y = x + 5
    return y

z = plus5(893)

print(z)


def summe(x, y):
    return x + y

y = summe(z, 6)
print(y)

z = summe("Hello ", "World!")

print(z)

def spacer():
    print("-----------------------------")

spacer()

def summe2(x = 5, y = 10):
    return x + y

print("summe2()")
print(summe2())
print("summe2(10)")
print(summe2(10))
print("summe2(y = 20)")
print(summe2(y = 20))
print("summe2()")
print(summe2())
