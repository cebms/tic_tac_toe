from game import Game

def main():
    game = Game()
    game.board.execute_move(1, (2,2))
    game.board.print()

if __name__ == '__main__':
    main()
