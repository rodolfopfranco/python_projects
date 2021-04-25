from board import Board
from gameFlow import GameFlow

def Main():
    g = GameFlow()
    b = Board()
    print(b)
    gameOver = False
    while(gameOver != True):
        b = g.selectJewel(b)
        print(b)
        if (b.getScore() >= g.getLvl1()) :
            gameOver = True
    print("Complete!")
    print("Score: ",b.getScore())

Main()