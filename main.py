from humanPlayer import humanPlayer
from Player import Player
from Grid import Grid

g1 = Grid()
h1 = humanPlayer()

h1.placeShip("A",5)
h1.placeShip("B",4)
h1.placeShip("C",3)
h1.placeShip("S",3)
h1.placeShip("D",2)
h1.printGrids()
