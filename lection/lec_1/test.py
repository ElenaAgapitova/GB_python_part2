# from turtle import *
#
# # speed(5)
# #
# # for step in 1, 2, 3, 4, 5, ..., 15:
# #     forward(120)
# #     right(720 / 5)
#
# speed(1)
#
# pensize(2)  # 3
#
# right(90)  # 4
# forward(100)  # 5
# right(90)  # 6
# forward(100)  # 7
# right(90)  # 8
# forward(100)  # 9
# right(90)  # 10
# forward(100)  # 11
#
# right(60)  # 12
# forward(57)  # 13
# right(60)  # 14 !!!
# forward(20)  # 15
#
# left(120)  # 16
# forward(20)  # 17
# right(90)  # 18
# forward(20)  # 19
# right(90)  # 20
# forward(20)  # 21
# forward(11)  # 22
# left(60)  # 23
# forward(14)  # 24
#
# penup()  # 25
# forward(50)  # 26
#
# exitonclick()


n = int(input())

if n > 0:
    for _ in range(n):
        for _ in range(n):
            print('*', end='')
        print()