import numpy as np
from typing import Tuple



class Board:
    def __init__(self):
        self.board = np.zeros((3,3), dtype=np.int8)
        self.shape = self.board.shape

    def __getitem__(self, coordinates):
       row, column = coordinates 
       return self.board[row, column]

    def __validate_move(self, piece: str, coordinates: Tuple):
        if piece != 1 and piece != 2:
            raise Exception("Piece argument must be 1 or 2")
        if(coordinates[0] < 0 or coordinates[1] < 0):
            raise Exception("Provide a positive value for x and y coordinates")
        if(coordinates[0] >= self.board.shape[1] or coordinates[1] >= self.board.shape[1]):
            raise Exception("Movement out of board range")
        if(self.board[coordinates[0]][coordinates[1]] != 0):
            raise Exception("Position occupied. Invalid play")

    def print(self):
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                print(self.board[i][j], end="")
                if j < (self.board.shape[1] - 1):
                    print("|", end="")
            print("")
        print("")

    def clear(self):
        self.board = np.zeros((3,3), dtype=np.int8)

    def execute_move(self, piece, coordinates: Tuple):
        self.__validate_move(piece, coordinates)
        self.board[coordinates[0]][coordinates[1]] = piece
