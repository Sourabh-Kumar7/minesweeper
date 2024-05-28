class Player:
    def __init__(self, board):
        self.board = board

    def reveal(self, row, col):
        return self.board.reveal_cell(row, col)

    def flag(self, row, col):
        self.board.flag_cell(row, col)
