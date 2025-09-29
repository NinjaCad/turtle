import math
run = True

while run:

    radius = int(input("Enter positive integer radius (0 to quit): "))

    if (radius == 0):

        print("Quitting program now...")
        run = False

    else:
        
        x = radius
        y = radius
        for yy in range(radius * 2 + 1):
            line = ''
            for xx in range(radius * 2 + 1):
                if (math.sqrt((xx - x) ** 2 + (yy - y) ** 2) <= radius):
                    line += '* '
                else:
                    line += '  '
            print(line)