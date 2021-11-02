
def shootAbove() :
    shoot(otherPlayer,x,y+1)
    if self.gridShots.returnLocation(x,y+1) == "0":
        self.verticalUp=True
    else :
        self.verticalUp = False
def shootLeft() :
    shoot(otherPlayer, x-1, y)
    if self.gridShots.returnLocation(x-1, y) == "0":
        self.verticalDown=True
    else :
        self.verticalUp = False
def shootRight() :
    shoot(otherPlayer, x+1, y)
    if self.gridShots.returnLocation(x+1, y) == "0":
        self.horizontalRight=True
    else :
        self.horizontalRight = False
def shootBelow() :
    shoot(otherPlayer, x, y - 1)
    if self.gridShots.returnLocation(x, y - 1) == "0":
        self.horizontalLeft=True
    else :
        self.HorizontalLeft = False

if justHit == True :
    if
    def shoot(self,otherPlayer, row,col):
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            if otherPlayer.gridShips.isSpaceWater(x, y):  # if space is water
                print("You hit water")
                self.gridShots.changeSingleSpace(x, y, "X")
                justHit = False
            elif otherPlayer.gridShots.returnLocation(x, y) == "X" or self.gridShots.returnLocation(x,y) == "0":  # turn has already been played
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
                justHit = True
                previousX = x
                previousY = y