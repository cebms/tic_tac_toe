from game import Game

def main():
    game = Game()
    game.board.execute_move(1, (2,2))
    game.board.execute_move(1, (1,2))
    game.board.execute_move(2, (0,0))
    game.board.execute_move(2, (0,1))
    game.board.print()
    print(game.find_ai_best_move())

if __name__ == '__main__':
    main()
