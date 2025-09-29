import turtle
import random

wn = turtle.Screen()
t = turtle.Turtle()

def main():
    r = int(random.random() * 100)/100
    g = int(random.random() * 100)/100
    b = int(random.random() * 100)/100

    wn.bgcolor(r, g, b)
    print("Random background color is: (", r, ",", g, ",", b, ")")

    copies = int(input("Enter rotational copies: "))
    sides = int(input("Enter sides per polygon: "))
    length = int(input("Enter edge pixel length: "))

    t.color("white")
    t.pensize(5)
    t.pendown()

    angle = 360 / copies
    for i in range(copies):
        makepolygons(t, sides, length)
        t.left(angle)

    print("Click turtle screen to exit...")
    wn.exitonclick()

def makepolygons(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

main()