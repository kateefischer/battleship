def alreadyHit(self, otherPlayer, col, row) :
    if otherPlayer.gridShots.returnLocation(col, row) == "X" or self.gridShots.returnLocation(col, row) == "0":
        return True
    else :
        return False

def validValue(self, col, row) :
    if (col < 10 and row < 10) and (col >=0 and row >= 0):
        return True
    else:
        return False


col = 1
row = 1
while (row < 10) :
    if self.stillHasShips == false :
        print ("you win")
        break
    if col > 9 :
        row = row+1
        col = 1
    else :
        if alreadyHit(otherPlayer, col, row):
            col = col + 2
        else :
            shoot(row, col)
            while (True):
                if otherPlayer.gridShots.returnLocation(x + 1 or x - 1, y) == "X":
                    horizontalHit()
                    break
                else:
                    verticalHit()
                    break
            break
col = 0
row = 0
while (row < 10) :
    if self.stillHasShips == false :
        print ("you win")
        break
    if col > 8 :
        row = row+1
        col = 0
    else :
        if alreadyHit(otherPlayer, col, row):
            col = col + 2
        else :
            shoot(row, col)
            while (True):
                if otherPlayer.gridShots.returnLocation(x + 1 or x - 1, y) == "X":
                    horizontalHit()
                    break
                else:
                    verticalHit()
                    break
            break


def shoot (self,otherPlayer, row,col) :
    if otherPlayer.gridShips.isSpaceWater(col, row):  # if space is water
        print("You hit water")
        self.gridShots.changeSingleSpace(col, row, "X")
    else:
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


def verticalHit(self, x):
    newx = x
    while (count < 1):
        if otherPlayer.gridShots.returnLocation(x + 1, y) == "X":
            x = x + 1
        else:
            count = count + 1
            break
    while (count < 2):
        x = newx
        if otherPlayer.gridShots.returnLocation(x - 1, y) == "X":
            x = x - 1
        else:
            count = count + 1
            break


def horizontalHit(self, y):
    newy = y
    while (count < 1):
        if otherPlayer.gridShots.returnLocation(x, y + 1) == "X":
            y = y + 1
        else:
            count = count + 1
            break
    while (count < 2):
        y = newy
        if otherPlayer.gridShots.returnLocation(x, y - 1) == "X":
            y = y - 1
        else:
            count = count + 1
            break