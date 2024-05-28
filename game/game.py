from game.board import Board
from game.player import Player

class MinesweeperGame:
    def __init__(self):
        self.board = Board()
        self.player = Player(self.board)

    def start(self):
        print("Welcome to Minesweeper!")
        self.board.print_board()
        while True:
            action = input("Enter action (R row col to reveal, F row col to flag): ").strip().split()
            if not action:
                continue
            command, row, col = action[0], int(action[1]), int(action[2])
            if command == 'R':
                if not self.player.reveal(row, col):
                    print("Game Over! You hit a mine.")
                    self.board.print_board(reveal_mines=True)
                    break
            elif command == 'F':
                self.player.flag(row, col)
            else:
                print("Invalid command.")
            self.board.print_board()
            if self.board.all_non_mine_cells_revealed() and self.board.all_mines_flagged():
                print("Congratulations! You've won the game.")
                self.board.print_board(reveal_mines=True)
                break
