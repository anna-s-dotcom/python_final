from turtle import *

clear()

right(90)
forward(100)
right(180)
forward(100)

speed(1)

def baum(l):
    print(l)
    if l > 10:
        forward(l)
        left(45)
        print('left', l)
        baum(l*0.6)
        right(90)
        print('right', l)
        baum(l*0.6)
        left(45)
        back(l)

baum(100)

# def baum(d, l):
#     if d > 0:
#         forward(l)
#         left(45)
#         baum(d -1, l*0.6)
#         right(90)
#         baum(d -1, l*0.6)
#         left(45)
#         back(l)
#
# baum(6, 100)

done()
