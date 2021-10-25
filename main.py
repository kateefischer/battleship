from Player import Player
from Grid import Grid
from ComputerPlayer import ComputerPlayer
from humanPlayer import humanPlayer

h = humanPlayer()
c = ComputerPlayer()
c.createShipGrid()
c.printGrids()
h.createShipGrid()
h.printGrids()
while (h.stillHasShips and c.stillHasShips()):
    h.takeTurn(c)
    c.takeTurn(h)
    c.printGrids()
    h.printGrids()