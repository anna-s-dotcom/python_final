# Summiere alle Zahlen von 0 - 10 auf.
# Nutze eine for - Schleife

# Bonus: lies zwei zahlen ein und summiere alle zahlen auf, die von
# zahl eins bis zahl zwei gehen.

sum = 0
for i in range(5):
    sum = sum + i
    #1+2=3+3=6+4=10

print(sum)

sum = 0
for i in range(11):
    sum += i

print(sum)


x = 5
y = 6

sum = 0
for i in range(x, y+1):
    sum += i

print(sum)
