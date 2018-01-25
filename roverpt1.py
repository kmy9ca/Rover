import turtle
import time
############## ROVER CLASS #############

class Rover:
    def __init__(self):
        self.direction = ""
        self.xPos = 0
        self.yPos = 0
        self.yFuture = 0
        self.xFuture = 0
        self.path = ""

    def Move(self):
        if self.direction == "N":
            self.yPos += 1
        if self.direction == "S":
            self.yPos -= 1
        if self.direction == "E":
            self.xPos += 1
        if self.direction == "W":
            self.xPos -= 1

    def RotateLeft(self):
        directions = ["N", "E", "S", "W"]
        if self.direction == directions[0]:
            self.direction = "W"
        else:
            self.direction = directions[directions.index(self.direction) - 1]

    def RotateRight(self):
        directions = ["N", "E", "S", "W"]
        if self.direction == directions[len(directions)-1]:
            self.direction = "N"
        else:
            self.direction = directions[directions.index(self.direction) + 1]




############### GRID SIZE ##############

SizeValid = False
while not SizeValid:
    xMaxStr,yMaxStr = input("Enter the coordinates of the grid separated by a space.").split()
    try:
        xMax = int(xMaxStr)
        yMax = int(yMaxStr)
        SizeValid = True
    except ValueError:
        print("Please enter a number.")


############### INPUT ROVER1 ############
ValidOrientation1 = False
ValidDirections = ["N", "E", "S", "W"]

while not ValidOrientation1:
    rov1XStr,rov1YStr,rov1DirectionStr = input("Enter the first rover's x-coordinate, y-coordinate, and direction.").split()
    try:
        rov1X = int(rov1XStr)
        rov1Y = int(rov1YStr)
        ValidDirections.index(rov1DirectionStr)
        if (0 <= rov1X <= xMax) and (0 <= rov1Y <= yMax):
            ValidOrientation1 = True
        else:
            print("Rover is off grid! \n")
    except ValueError:
        print("Invalid location and/or orientation.")

Rover1 = Rover()
Rover1.direction = rov1DirectionStr
Rover1.xPos = rov1X
Rover1.yPos = rov1Y


######### ROVER 1 PATH #################
ValidMovements = ["R", "L", "M"]

rov1Path = input("What path will Rover 1 take?")

for i in rov1Path:
    if i not in ValidMovements:
        print("Invalid instruction given.")
Rover1.path = rov1Path

############# TURTLE ####################
Turtle1 = turtle.Turtle()
Turtle1.setposition(Rover1.xPos,Rover1.yPos)
if Rover1.direction == "N":
    Turtle1.left(90)
if Rover1.direction == "W":
    Turtle1.left(180)
if Rover1.direction == "S":
    Turtle1.right(90)

######### CALCULATE ROVER 1 FINAL POSITION ###########

for d in Rover1.path:
    if d == "L":
        Turtle1.left(90)
        Rover1.RotateLeft()
    if d == "R":
        Turtle1.right(90)
        Rover1.RotateRight()
    if d == "M":
        Turtle1.forward(10)
        Rover1.Move()
turtle.done()
print(Rover1.xPos, " ", Rover1.yPos, " ", Rover1.direction)


############### INPUT ROVER2 ############
ValidOrientation2 = False

while not ValidOrientation2:
    rov2XStr,rov2YStr,rov2DirectionStr = input("Enter the second rover's x-coordinate, y-coordinate, and direction.").split()
    try:
        rov2X = int(rov2XStr)
        rov2Y = int(rov2YStr)
        ValidDirections.index(rov2DirectionStr)
        if (0 <= rov2X <= xMax) and (0 <= rov2Y <= yMax):
            ValidOrientation2 = True
        else:
            print("Rover is off grid! \n")
    except ValueError:
        print("Invalid location and/or orientation.")
Rover2 = Rover()
Rover2.direction = rov2DirectionStr
Rover2.xPos = rov2X
Rover2.yPos = rov2Y



################# ROVER 2 PATH ###################
rov2Path = input("What path will Rover 2 take?")

for i in rov2Path:
    if i not in ValidMovements:
        print("Invalid instruction given.")
Rover2.path = rov2Path

############# TURTLE ####################
'''
Turtle2 = turtle.Turtle()
Turtle2.setposition(Rover2.xPos,Rover2.yPos)
if Rover2.direction == "N":
    Turtle2.left(90)
if Rover2.direction == "W":
    Turtle2.left(180)
if Rover2.direction == "S":
    Turtle2.right(90)
'''

############# CALCULATE ROVER 2 POSITION ###########
for d in Rover2.path:
    if d == "L":
        #Turtle2.left(90)
        Rover2.RotateLeft()
    if d == "R":
       # Turtle2.right(90)
        Rover2.RotateRight()
    if d == "M":
        #Turtle2.forward(10)
        Rover2.Move()

print(Rover2.xPos, " ", Rover2.yPos, " ", Rover2.direction)

#Turtle2.done()