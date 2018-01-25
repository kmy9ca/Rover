
############## ROVER CLASS #############

class Rover:
    def __init__(self):
        self.direction = ""
        self.xPos = 0
        self.yPos = 0
        self.yFuture = 0
        self.xFuture = 0

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

    def NextSpaceOnGrid(self):
        if self.direction == "N":
            self.xFuture = self.xPos
            self.yFuture = self.yPos + 1
        if self.direction == "E":
            self.xFuture = self.xPos + 1
            self.yFuture = self.yPos
        if self.direction == "S":
            self.xFuture = self.xPos
            self.yFuture = self.yPos - 1
        if self.direction == "W":
            self.xFuture = self.xPos - 1
            self.yFuture = self.yPos

    def RevertTest(self):
        if self.direction == "N":
            self.xFuture = self.xPos
            self.yFuture = self.yPos - 1
        if self.direction == "E":
            self.xFuture = self.xPos - 1
            self.yFuture = self.yPos
        if self.direction == "S":
            self.xFuture = self.xPos
            self.yFuture = self.yPos + 1
        if self.direction == "W":
            self.xFuture = self.xPos + 1
            self.yFuture = self.yPos

##### OBJECTS & IMPORTANT VARIABLES #####
UsedSpaces = []
rov1str = ""
rov2str = ""

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


########### ADD CURRENT POSITION TO LIST ######
TotalSpaces = (xMax + 1) * (yMax + 1)                           # this is the final size of the array
UsedSpaces.append([Rover1.xPos,Rover1.yPos])
UsedSpaces.append([Rover2.xPos,Rover2.yPos])

########## CHECK TO AVOID COLLISONS ##########
if Rover1.yPos == Rover2.yPos:
    if Rover1.yPos == 0:                                        # if both are on the bottom line
        while Rover1.direction != "N":                          # change Rover1 direction to North so it can move up
            Rover1.RotateLeft()
            rov1str += "L"
        Rover1.Move()                                           # move to line above
        rov1str += "M"
        UsedSpaces.append([Rover1.xPos, Rover1.yPos]) #added
    else:                                                       # if both on same line (not bottom)
        while Rover1.direction != "S":                          # make the Rover face south
            Rover1.RotateLeft()
            rov1str += "L"
        Rover1.Move()                                           # move to line below
        UsedSpaces.append([Rover1.xPos, Rover1.yPos])  #added
        rov1str += "M"



########### MOVE ROVER 1 TO TOP LEFT ######
while Rover1.direction != "W":  # face west
    Rover1.RotateLeft()
    rov1str += "L"
while Rover1.xPos != 0:         # move to left side
    Rover1.Move()
    UsedSpaces.append([Rover1.xPos,Rover1.yPos])
    rov1str += "M"

Rover1.RotateRight()            # face north
rov1str += "R"

while Rover1.yPos != yMax:      # move to top left
    Rover1.Move()
    UsedSpaces.append([Rover1.xPos, Rover1.yPos])
    rov1str += "M"
Rover1.RotateRight()            # face (likely) empty spaces

########## MOVE ROVER 2 TO BOTTOM RIGHT #####
while Rover2.direction != "E":  # face east
    Rover2.RotateLeft()
    rov2str += "L"
while Rover2.xPos != xMax:         # move to right side
    Rover2.Move()
    UsedSpaces.append([Rover2.xPos,Rover2.yPos])
    rov2str += "M"

Rover2.RotateRight()            # face south
rov2str += "R"

while Rover2.yPos != 0:      # move to bottom right
    Rover2.Move()
    UsedSpaces.append([Rover2.xPos, Rover2.yPos])
    rov2str += "M"
Rover2.RotateRight()            # face (likely) empty spaces


#### MOVE AROUND GRID FROM CORNERS #####

while len(UsedSpaces) < TotalSpaces:
    Rover1.NextSpaceOnGrid()

    if((0 <= Rover1.xFuture <= xMax) and (0 <= Rover1.yFuture <= yMax)):
        if([Rover1.xFuture, Rover1.yFuture] not in UsedSpaces):
            UsedSpaces.append([Rover1.xFuture,Rover1.yFuture])
            Rover1.Move()
            rov1str += "M"
        else:
            Rover1.RotateRight()
            rov1str += "R"
            Rover1.RevertTest()
    else:
        Rover1.RotateRight()
        rov1str += "R"
        Rover1.RevertTest()

    Rover2.NextSpaceOnGrid()

    if((0 <= Rover2.xFuture <= xMax) and (0 <= Rover2.yFuture <= yMax)):
        if([Rover2.xFuture, Rover2.yFuture] not in UsedSpaces):
            UsedSpaces.append([Rover2.xFuture,Rover2.yFuture])
            Rover2.Move()
            rov2str += "M"
        else:
            Rover2.RotateLeft()
            rov2str += "L"
            Rover2.RevertTest()
    else:
        Rover2.RotateLeft()
        rov2str += "L"
        Rover2.RevertTest()

print(rov1str)
print(rov2str)
print('\n')
#print (UsedSpaces)
