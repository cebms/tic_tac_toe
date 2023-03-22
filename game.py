from board import Board


class Game:
    def __init__(self):
        self.board = Board()

    def evaluate(self):

        for i in range(self.board.shape[0]): #Checking rows
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2]:
                if self.board[i, 0] == 1:
                    return 1
                elif self.board[i, 0] == 2:
                    return -1
        
        for i in range(self.board.shape[1]): #Checking columns
            if self.board[0, i] == self.board[1, i] == self.board[2, i]:
                if self.board[0, i] == 1:
                    return 1
                elif self.board[0, i] == 2:
                    return -1

        if self.board[0,0] == self.board[1,1] == self.board[2,2]: #Checking main diagonal
            if self.board[0,0] == 1:
                return 1
            elif self.board[0,0] == 2:
                return -1

        if self.board[0, 2] == self.board[1, 1] and self.board[2, 0]: #Checking secondary diagonal
            if self.board[2, 0] == 1:
                return 1
            elif self.board[2, 0] == 2:
                return -1

        return 0

    def reset(self):
        self.board.clear()
