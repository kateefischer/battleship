from player import player and grid


def takeTurn(self,otherPlayer):


def placeShip(self,ship,size):
    row = int(input("Please enter the a row number"))
    col = int(input("Please enter a column number"))
        while (row>10):
            row = int(input("Please enter the a row number"))
        while (col>10):
            col = int(input("Please enter a column number"))

    direction = str(input("Please enter either horizontal or vertical"))
    size = str(input("Please enter a ship "))
    a=1;
    while (a <= size):
        if self.gridship.isSpaceWater(self, row, col)==False:
            self.changeRow(self , row , value , colStart , size )
            self.changeCol(self, row, value, colStart, size)

        else:
            row = row+1
            col = col +1





