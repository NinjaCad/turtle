import turtle

wn = turtle.Screen()
turtle = turtle.Turtle()

angle = int(input("Enter int angle: "))
ran = int(input("Enter int range: "))
print("Click turtle screen to exit...")

for i in range(ran - 1):
    turtle.forward(i)
    turtle.left(angle)
    
wn.exitonclick()