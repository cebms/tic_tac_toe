from game import Game

def main():
    game = Game()
    while(True):
        game.board.print()
        row, column = input("Your move: ").split()
        row = int(row)
        column = int(column)
        game.board.execute_move(2, (row, column))
        game.board.execute_move(1, game.find_ai_best_move())



if __name__ == '__main__':
    main()
