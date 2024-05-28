from game.board import Board
from game.player import Player


class MinesweeperGame:
    def __init__(self):
        self.board = Board()
        self.player = Player(self.board)

    def start(self):
        print("Welcome to Minesweeper!")
        self.board.print_board()
        print("Enter 'exit' to quit the game.")

        while True:
            action = input("Enter action (R row col to reveal, F row col to flag): ").strip().split()

            if len(action) == 1 and action[0].lower() == 'exit':
                print("Thanks for playing! Goodbye.")
                break

            if len(action) != 3:
                print("Invalid input format. Correct format: R row col or F row col. Example: R 1 1 or F 2 2")
                continue

            command, row, col = action[0], action[1], action[2]

            if not (command in ['R', 'F'] and row.isdigit() and col.isdigit()):
                print("Invalid input format. Correct format: R row col or F row col. Example: R 1 1 or F 2 2")
                continue

            row, col = int(row), int(col)
            if not (0 <= row < self.board.size and 0 <= col < self.board.size):
                print(f"Invalid row or column. Please enter numbers between 0 and {self.board.size - 1}.")
                continue

            if command == 'R':
                if not self.player.reveal(row, col):
                    print("Game Over! You hit a mine.")
                    self.board.print_board(reveal_mines=True)
                    break
            elif command == 'F':
                self.player.flag(row, col)

            self.board.print_board()

            if self.board.all_non_mine_cells_revealed() and self.board.all_mines_flagged():
                print("Congratulations! You've won the game.")
                self.board.print_board(reveal_mines=True)
                break
