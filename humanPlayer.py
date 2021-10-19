from Player import Player

class HumanPlayer(Player):

    def placeShips(self, ship):  # places ships
        while (True):
            row = int(input("Enter the coordinate of the row where ship starts"))
            col = int(input("Enter the coordinate of the col where ship starts"))
            direction = input("Horizontal (H) or Vertical? (V)")
            if (row>10 or col>10 or row<0 or col<0):  # if the placement is out of bounds for both the col and rows
                continue
            direction = direction.upper()
            if (direction != "V" and direction != "H"):  # if direction is invalid
                continue
            inGrid = self.checkLegalPlacement(row, col, direction, ship)
            if (inGrid == False):  # if placed invalidly
                continue
            self.placeShipInGrid(row, col, direction, ship)
            break


    def takeTurn(self):
        while (True):
            rowGuess = random.randint(0, 10)
            colGuess = random.randint(0, 10)
            if self.legalGuess(rowGuess, colGuess) == False:
                continue
        return [rowGuess, colGuess]





