from board import Board


class Game:
    def __init__(self):
        self.ai_player = 1
        self.opponent = 2
        self.board = Board()

    def __possible_moves(self):
        moves = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if(self.board[i, j] == 0):
                    moves.append((i, j))
        return moves

    def __evaluate_board(self):
        for i in range(self.board.shape[0]): #Checking rows
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2]:
                if self.board[i, 0] == 1:
                    return 10
                elif self.board[i, 0] == 2:
                    return -10
        
        for i in range(self.board.shape[1]): #Checking columns
            if self.board[0, i] == self.board[1, i] == self.board[2, i]:
                if self.board[0, i] == 1:
                    return 10
                elif self.board[0, i] == 2:
                    return -10

        if self.board[0,0] == self.board[1,1] == self.board[2,2]: #Checking main diagonal
            if self.board[0,0] == 1:
                return 10
            elif self.board[0,0] == 2:
                return -10

        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0]: #Checking secondary diagonal
            if self.board[2, 0] == 1:
                return 10
            elif self.board[2, 0] == 2:
                return -10

        return 0

    def is_board_full(self):
        game_over = True
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if(self.board[i, j] == 0):
                    return False
        return game_over        

    def __minimax(self, subtree_height, is_ai_turn):
        board_score = self.__evaluate_board()

        if(board_score == 10): #maximizer won
            return board_score - subtree_height

        if(board_score == -10): #minimizer won
            return board_score + subtree_height

        if(self.is_board_full() == True): #it's a draw
            return 0
        

        if(is_ai_turn == True): #should maximize
            best_move_evaluation = float('-inf')

            for move in self.__possible_moves():
                self.board[move[0], move[1]] = self.ai_player
                best_move_evaluation = max(best_move_evaluation, self.__minimax(subtree_height + 1, False)) #makes the move and evaluates consequences
                self.board[move[0], move[1]] = 0
            return best_move_evaluation
        else: #should minimize
            best_move_evaluation = float('inf')

            for move in self.__possible_moves():
                self.board[move[0], move[1]] = self.opponent
                best_move_evaluation = min(best_move_evaluation, self.__minimax(subtree_height + 1, True))
                self.board[move[0], move[1]] = 0
            return best_move_evaluation

    def find_ai_best_move(self):
        best_move_value = float('-inf')
        best_move = () #(row, column)

        #for the current board, evaluate the result of playing on each empty slot
        for move in self.__possible_moves():
            self.board[move[0], move[1]] = self.ai_player #ai's move
            current_move_value = self.__minimax(0, False) #compute possible opponent moves

            self.board[move[0], move[1]] = 0

            if(current_move_value > best_move_value):
                best_move_value = current_move_value
                best_move = (move[0], move[1])
        
        return best_move

    def reset(self):
        self.board.clear()
