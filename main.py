import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)


color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107),
              (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
              (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169),
              (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]

number_of_dots = 80
ninja_turtle = Turtle()


def make_dot():
    ninja_turtle.dot(30, random.choice(color_list))
    ninja_turtle.forward(70)


ninja_turtle.speed(0)
ninja_turtle.up()
ninja_turtle.setheading(210)
ninja_turtle.forward(400)
ninja_turtle.setheading(0)
ninja_turtle.hideturtle()


for dot_counts in range(1, number_of_dots + 1):
    make_dot()

    if dot_counts % 10 == 0:
        ninja_turtle.setheading(90)
        ninja_turtle.fd(70)
        ninja_turtle.setheading(180)
        ninja_turtle.fd(700)
        ninja_turtle.setheading(0)


screen.exitonclick()
