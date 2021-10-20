import random
from Player import Player

class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.aCount = 5
        self.bCount = 4
        self.cCount = 3
        self.sCount = 3
        self.dCount = 2

    def takeTurn(self, otherPlayer):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        if otherPlayer.isSpaceWater(x, y):  # if space is water
            print("You hit water")
            self.gridShots.changeSingleSpace(x, y, "X")
        elif otherPlayer.returnLocation(x, y) == "X" or self.gridShots.returnLocation(x,y) == "0":  # turn has already been played
            self.takeTurn()
        else: # ship has been hit
            print("You hit a ship")
            if otherPlayer.returnLocation(x, y) == "A": # a ship hit
                self.aCount = self.aCount - 1
                if self.aCount == 0: # all as hit
                    print("You sunk the A ship")
            elif otherPlayer.returnLocation(x, y) == "B": # b ship hit
                self.bCount = self.bCount - 1
                if self.bCount == 0: # all bs hit
                    print("You sunk the B ship")
            elif otherPlayer.returnLocation(x, y) == "C": # c ship hit
                self.cCount = self.cCount - 1
                if self.cCount == 0: # all cs hit
                    print("You sunk the C ship")
            elif otherPlayer.returnLocation(x, y) == "S": # s ship hit
                self.sCount = self.sCount - 1
                if self.sCount == 0: # all ss hit
                    print("You sunk the S ship")
            else: # d ship hit
                self.dCount = self.dCount - 1
                if self.dCount == 0: # all ds hit
                    print("You sunk the D ship")
            self.gridShots.changeSingleSpace(x, y, "0")

    def placeShip(self, ship, size):
        s = 1
        isVert = random.randint(0, 2)
        vertical = False
        if (isVert == 0):  # randomly decide if vertical
            vertical = True
        if vertical: # if vertical
            x = random.randint(0, 9)
            initialY = random.randint(0, (9 - (size + 1)))  # so it fits
            y = initialY
            print (y,x)
            s = 0
            while s < size : #check to make sure none overlap
                if not self.gridShips.isSpaceWater(y,x) : #if ship already there
                    self.gridShips.placeShip(ship,size)
                s = s+1
                y = y+1
            self.gridShips.changeCol(x, ship, initialY, size)
        else: # if horizontal
            initialX = random.randint(0, (9 - (size + 1)))  # so it fits
            y = random.randint(0, 9)
            x = initialX
            print(y, x)
            s = 0
            while s < size : #check to make sure none overlap
                if not self.gridShips.isSpaceWater(y,x) : #if ship already there
                    self.gridShips.placeShip(ship,size)
                s = s+1
                x = x+1
            self.gridShips.changeRow(y, ship, initialX, size)

    def stillHasShips(self):
        if self.aCount == 0 and self.bCount == 0 and self.cCount == 0 and self.sCount == 0 and self.dCount == 0: # if no ships left
            return False
        else: # ships left
            return True
