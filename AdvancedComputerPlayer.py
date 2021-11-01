import random
from Player import Player

class AdvancedComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.aCount = 5
        self.bCount = 4
        self.cCount = 3
        self.sCount = 3
        self.dCount = 2

    def takeTurn(self, otherPlayer):
        col = 1
        row = 0
        x = 0
        i = 1
        a = 2
        while (x < 50) :
            if otherPlayer.gridShips.isSpaceWater(col, row):  # if space is water
                print("You hit water")
                self.gridShots.changeSingleSpace(col, row, "X")
            elif otherPlayer.gridShots.returnLocation(col, row) == "X" or self.gridShots.returnLocation(col, row) == "0":  # turn has already been played
                self.takeTurn()

            else: # ship has been hit
                print("You hit a ship")
                if otherPlayer.gridShots.returnLocation(x, y) == "A": # a ship hit
                    self.aCount = self.aCount - 1
                    if self.aCount == 0: # all as hit
                        print("You sunk the A ship")
                elif otherPlayer.gridShots.returnLocation(x, y) == "B": # b ship hit
                    self.bCount = self.bCount - 1
                    if self.bCount == 0: # all bs hit
                      print("You sunk the B ship")
                elif otherPlayer.gridShots.returnLocation(x, y) == "C": # c ship hit
                    self.cCount = self.cCount - 1
                    if self.cCount == 0: # all cs hit
                      print("You sunk the C ship")
                elif otherPlayer.gridShots.returnLocation(x, y) == "S": # s ship hit
                    self.sCount = self.sCount - 1
                    if self.sCount == 0: # all ss hit
                      print("You sunk the S ship")
                else: # d ship hit
                    self.dCount = self.dCount - 1
                    if self.dCount == 0: # all ds hit
                        print("You sunk the D ship")
                self.gridShots.changeSingleSpace(x, y, "0")
            x = x+1
            if ((col-1)<10 and (col-1)>=0) and ((row+1)<10 and (row+1)>=0) :
                col = col-1
                row = row+1
            else :
                i = i+2
                if (i >= 5):
                    col = 9
                    row = a
                    a = a + 2
                else:
                    col = i
                    row = 0
            if otherPlayer.StillHasShips() :
                continue
            else :
                break
        col = 0
        row = 0
        x = 0
        i = 0
        a = 1
        while (x < 50):
            if otherPlayer.gridShips.isSpaceWater(col, row):  # if space is water
                print("You hit water")
                self.gridShots.changeSingleSpace(col, row, "X")
            elif otherPlayer.gridShots.returnLocation(col, row) == "X" or self.gridShots.returnLocation(col,
                                                                                                        row) == "0":  # turn has already been played
                self.takeTurn()

            else:  # ship has been hit
                print("You hit a ship")
                if otherPlayer.gridShots.returnLocation(x, y) == "A":  # a ship hit
                    self.aCount = self.aCount - 1
                    if self.aCount == 0:  # all as hit
                        print("You sunk the A ship")
                elif otherPlayer.gridShots.returnLocation(x, y) == "B":  # b ship hit
                    self.bCount = self.bCount - 1
                    if self.bCount == 0:  # all bs hit
                        print("You sunk the B ship")
                elif otherPlayer.gridShots.returnLocation(x, y) == "C":  # c ship hit
                    self.cCount = self.cCount - 1
                    if self.cCount == 0:  # all cs hit
                        print("You sunk the C ship")
                elif otherPlayer.gridShots.returnLocation(x, y) == "S":  # s ship hit
                    self.sCount = self.sCount - 1
                    if self.sCount == 0:  # all ss hit
                        print("You sunk the S ship")
                else:  # d ship hit
                    self.dCount = self.dCount - 1
                    if self.dCount == 0:  # all ds hit
                        print("You sunk the D ship")
                self.gridShots.changeSingleSpace(x, y, "0")
            x = x + 1
            if ((col - 1) < 10 and (col - 1) >= 0) and ((row + 1) < 10 and (row + 1) >= 0):
                col = col - 1
                row = row + 1
            else:
                i = i + 2
                if (i >= 5):
                    col = 9
                    row = a
                    a = a + 2
                else:
                    col = i
                    row = 0
            if otherPlayer.StillHasShips():
                continue
            else:
                break



    def placeShip(self, ship, size):
        while True:
            isVert = random.randint(0, 1)
            if (isVert == 0): # if vertical
                col = random.randint(0, 9)
                row = random.randint(0, (9 - size)) # so it fits
                if self.canBePlaced(1,row,col,size) :
                    self.gridShips.changeCol(col, ship, row, size)
                    break
                else :
                    continue
            else: # if horizontal
                col = random.randint(0, (9 - size))  # so it fits
                row = random.randint(0, 9)
                if self.canBePlaced(0, row, col, size):
                    self.gridShips.changeRow(row, ship, col, size)
                    break
                else:
                    continue

    def stillHasShips(self):
        if self.aCount == 0 and self.bCount == 0 and self.cCount == 0 and self.sCount == 0 and self.dCount == 0: # if no ships left
            return False
        else: # ships left
            return True

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
