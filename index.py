import turtle

def createLSystem(iterations, axiom):
    startstring = axiom
    endstring = ""
    for i in range(iterations):
        endstring = processString(startstring)
        startstring = endstring
        print(i, "\t", startstring)
    return endstring

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr += applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    contains = False
    for rule in rules:
        if ch == rule[0]:
            newstr = rule[1]
            contains = True
    if not contains:
        newstr = ch
    return newstr

def drawLsystem(t, instructions, angle, length):
    stack = []
    for cmd in instructions:
        if cmd == 'F':
            t.forward(length)
        elif cmd == 'B':
            t.backward(length)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
        elif cmd == '>':
            t.pensize(t.pensize() + 1)
        elif cmd == '<':
            t.pensize(max(1, t.pensize() - 1))
        elif cmd == '[':
            state = (t.position(), t.heading(), t.pensize())
            stack.append(state)
        elif cmd == ']':
            state = stack.pop()
            t.penup()
            t.goto(state[0])
            t.setheading(state[1])
            t.pensize(state[2])
            t.pendown()

def main():
    print("Symbols: 'F'=MoveForward")
    print("", '\t', "'B'=MoveBackward")
    print("", '\t', "'+'=TurnRight")
    print("", '\t', "'-'=TurnLeft")
    print("", '\t', "'>'=PenWider,")
    print("", '\t', "'<'=PenNarrower,")
    print("", '\t', "'['=StateSave,")
    print("", '\t', "']'=StateRestore,")
    print("", '\t', "'ACDEGHIJKLMNOPQRSTUVWXYZ'=TurtleIgnores")

    #iterations = int(input("Enter iterations: "))
    #length = float(input("Enter length: "))
    #angle = float(input("Enter angle: "))
    #axiom = input("Enter axiom: ")

    iterations = 6
    length = 3
    angle = 11.25
    axiom = "--------X"

    loop = False
    #loop = True
    while loop:
        newrule = input("Enter new rule 'LHS -> RHS' (empty line to exit): ")
        if newrule == "":
            loop = False
        elif newrule.count("->") == 1:
            lhs, rhs = newrule.split("->")
            rules.append([lhs.strip(), rhs.strip()])

    rules.append(['X', 'F[---X]F[++X]-X'])
    rules.append(['F', '>>FF<<'])

    inst = createLSystem(iterations, axiom)
    print(inst)

    t = turtle.Turtle()
    t.penup()
    wn = turtle.Screen()
    t.pensize(1)
    t.speed(0)
    t.goto(0, -200)
    t.pendown()
    t.hideturtle()

    drawLsystem(t, inst, angle, length)
    wn.exitonclick()

rules = []
main()
