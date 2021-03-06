from Player import Player

class humanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.countA = 0
        self.countB = 0
        self.countC = 0
        self.countS = 0
        self.countD = 0

    def placeShip(self, ship, size):  # places ships
        self.printGrids()
        while (True):
            print("Lets place your ship that is ", size, "places")
            row = int(input("Enter the coordinate of the row where ship starts"))
            col = int(input("Enter the coordinate of the col where ship starts"))
            direction = int(input("Horizontal (1) or Vertical? (0)"))
            if row>9 or row<0 or col>9 or row<0:
                print("invalid entry try again!")
                continue
            if direction == 1 and col + size > 10 :
                print("invalid entry try again!")
                continue
            if direction ==0 and row +size>10:
                print("invalid entry try again!")
                continue
            if direction == 1:
                if self.canBePlaced(1,row,col,size):
                    self.gridShips.changeRow(row,ship,col,size)
                    break
                else:
                    print("invalid entry try again!")
                    continue
            else:
                if self.canBePlaced(0,row,col,size):
                    self.gridShips.changeCol(col,ship,row,size)
                    break
                else:
                    print("invalid entry try again!")
                    continue

    def canBePlaced(self, isVertical, row, col, size):
        if isVertical == 1 :
            for r in range (size) :
                if not self.gridShips.isSpaceWater(row+r, col) :
                    return False
        else :
            for c in range(size):
                if not self.gridShips.isSpaceWater(row, col+c) :
                    return False
        return True

    def takeTurn(self, otherPlayer): #pick a square and put something down
        while (True):
            rowGuess = int(input("Please enter your guess for the row"))
            colGuess = int(input("Please enter your guess for the column"))
            if otherPlayer.gridShips.isSpaceWater(rowGuess, colGuess):  # if space is water
                print("You hit water")
                self.gridShots.changeSingleSpace(rowGuess, colGuess, "X")
                break
            elif otherPlayer.gridShots.returnLocation(rowGuess, colGuess) == "X" or self.gridShots.returnLocation(rowGuess,colGuess) == "0":  # turn has already been played
                self.takeTurn(otherPlayer)
            else:  # ship has been hit
                print("You hit a ship")
                if otherPlayer.gridShots.returnLocation(rowGuess, colGuess) == "A":  # if it is ship A
                    print("You hit a ship")
                    self.countA = 1 + self.countA
                    if self.countA >= 5:  # if the ship is completely hit
                        print("you suck the A ship")
                if otherPlayer.gridShots.returnLocation(rowGuess, colGuess) == "B":  # if it is ship B
                    print("You hit a ship")
                    self.countB = 1 + self.countB
                    if self.countB >= 4:  # if the ship is completely hit
                        print("you suck the B ship")
                if otherPlayer.gridShots.returnLocation(rowGuess, colGuess) == "C":  # if it is ship C
                    print("You hit a ship")
                    self.countC = 1 + self.countC
                    if self.countC >= 3:  # if the ship is completely hit
                        print("you suck the C ship")
                if otherPlayer.gridShots.returnLocation(rowGuess, colGuess) == "S":  # if it is ship S
                    print("You hit a ship")
                    self.countS = 1 + self.countS
                    if self.countS >= 3:  # if the ship is completely hit
                        print("you suck the S ship")
                if otherPlayer.gridShots.returnLocation(rowGuess, colGuess) == "D":  # if it is ship D
                    print("You hit a ship")
                    self.countD = 1 + self.countD
                    if self.countD >= 2:  # if the ship is completely hit
                        print("you suck the D ship")
                break
                self.gridShots.changeSingleSpace(rowGuess, colGuess, "0")


    def stillHasShips(self):
        if self.countA == 5 and self.countB == 4 and self.countC == 3 and self.countS == 3 and self.countD == 2:  # if no ships left
            return False
        else:  # ships left
            return True





    def canBePlaced(self, direction, row, col, size):
        if direction == 1:
            for r in range(size):
                if not self.gridShips.isSpaceWater(row+r, col):
                    return False
        else:
            for c in range(size):
                if not self.gridShips.isSpaceWater(row, col+c):
                    return False
        return True













