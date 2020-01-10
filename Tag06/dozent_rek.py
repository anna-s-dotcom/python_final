from turtle import *

clear()

def spirale(x):
    if x > 10:
        spirale(x*0.9)
        forward(x)
        left(90)

def spirale(x):
    if x <= 10:
        return
    else:
        spirale(x*0.9)
        forward(x)
        left(90)

spirale(200)

done()
