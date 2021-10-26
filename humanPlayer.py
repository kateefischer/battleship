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

            if direction == 1:
                if self.canBePlaced(direction,row,col,size):
                    self.gridShips.changeRow(row,ship,col,size)
                    break
                else:
                    print("invalid entry try again!")
                    continue
            else:
                if self.canBePlaced(direction,row,col,size):
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
            if (rowGuess < 0 or rowGuess > 9):  # if guess is out of bounds
                continue
            if (rowGuess < 0 or rowGuess > 9):  # if guess is out of bounds
                continue
            if self.gridShots[rowGuess, colGuess] == "-" or self.gridShots[rowGuess, colGuess] == "~": # out of bounds
                continue
            if otherPlayer.returnLocation(rowGuess,colGuess)== "A": #if it is ship A
                print("You hit a ship")
                self.countA = 1+self.countA
                if self.countA>=5: # if the ship is completely hit
                    print("you suck the A ship")
            if otherPlayer.returnLocation(rowGuess,colGuess)== "B": # if it is ship B
                print("You hit a ship")
                self.countB = 1+self.countB
                if self.countB>=4: # if the ship is completely hit
                    print("you suck the B ship")
            if otherPlayer.returnLocation(rowGuess,colGuess)== "C": #if it is ship C
                print("You hit a ship")
                self.countC = 1+self.countC
                if self.countC>=3:# if the ship is completely hit
                    print("you suck the C ship")
            if otherPlayer.returnLocation(rowGuess,colGuess)== "S": # if it is ship S
                print("You hit a ship")
                self.countS = 1+self.countS
                if self.countS>=3:# if the ship is completely hit
                    print("you suck the S ship")
            if otherPlayer.returnLocation(rowGuess,colGuess)== "D": # if it is ship D
                print("You hit a ship")
                self.countD = 1+self.countD
                if self.countD>=2:# if the ship is completely hit
                    print("you suck the D ship")
            if otherPlayer.returnLocation(rowGuess,colGuess)=="~": #if they did not hit anything
                print("You did not hit anything")
            self.gridShots.changeSingleSpace(rowGuess, colGuess, "0")

    def stillHasShips(self):
        if self.CountA == 5 and self.CountB == 4 and self.CountC == 3 and self.CountS == 3 and self.CountD == 2:  # if no ships left
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












