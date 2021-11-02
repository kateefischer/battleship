from Player import Player
from Grid import Grid
from AdvancedComputerPlayer2 import AdvancedComputerPlayer2
from humanPlayer import humanPlayer

h = humanPlayer()
c = AdvancedComputerPlayer2()
c.createShipGrid()
c.printGrids()
h.createShipGrid()
h.printGrids()
while (h.stillHasShips() and c.stillHasShips()):
    c.takeTurn(h)
    c.printGrids()
    h.takeTurn(c)
    h.printGrids()