from time import sleep
import numpy as np
from scipy import signal
from icecream import ic
import os

class GameOfLifeBoard():
    def __init__(self) -> None:
        self.dim = 10
        self.board = np.zeros((self.dim, self.dim), dtype=np.int16)
        self.stalemate = False
        ic(self.board.shape)
        self.kernel = np.array( [[1,1,1], [1,1,1], [1,1,1]])
    def timestep(self):
        if not self.stalemate:
            temp = self.board
            self.board = signal.convolve2d(self.board, self.kernel, mode='same')
            # ic(self.board)
            self.board[self.board<3] = self.board[self.board>4] = 0
            self.board[self.board>=3] = 1
            ic(temp==self.board)
            # if (temp==self.board).all():
            #     self.stalemate=True

if __name__=="__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    newgame = GameOfLifeBoard()
    newgame.board[4:6,5] = 1
    # for i in range(10):
    while(True):
        ic(newgame.board)
        newgame.timestep()
        sleep(0.5)