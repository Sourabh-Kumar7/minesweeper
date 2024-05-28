import random

class Board:
    def __init__(self, size=10, mines=10):
        self.size = size
        self.mines_count = mines
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.mines = set()
        self.flags = set()
        self.revealed = set()
        self._place_mines()

    def _place_mines(self):
        while len(self.mines) < self.mines_count:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in self.mines:
                self.mines.add((row, col))
                self.grid[row][col] = '*'

    def reveal_cell(self, row, col):
        if (row, col) in self.mines:
            return False
        self._reveal(row, col)
        return True

    def _reveal(self, row, col):
        if (row, col) in self.revealed:
            return
        self.revealed.add((row, col))
        mine_count = self._adjacent_mines(row, col)
        if mine_count == 0:
            self.grid[row][col] = ' '
            for r, c in self._adjacent_cells(row, col):
                if self.grid[r][c] == ' ':
                    self._reveal(r, c)
        else:
            self.grid[row][col] = str(mine_count)

    def _adjacent_mines(self, row, col):
        return sum((r, c) in self.mines for r, c in self._adjacent_cells(row, col))

    def _adjacent_cells(self, row, col):
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < self.size and 0 <= c < self.size:
                    yield r, c

    def flag_cell(self, row, col):
        if (row, col) not in self.flags:
            self.flags.add((row, col))

    def unflag_cell(self, row, col):
        if (row, col) in self.flags:
            self.flags.remove((row, col))

    def all_non_mine_cells_revealed(self):
        return len(self.revealed) == self.size * self.size - self.mines_count

    def all_mines_flagged(self):
        return self.mines == self.flags

    def print_board(self, reveal_mines=False):
        for r in range(self.size):
            for c in range(self.size):
                if (r, c) in self.revealed or reveal_mines and self.grid[r][c] == '*':
                    print(self.grid[r][c], end=' ')
                elif (r, c) in self.flags:
                    print('F', end=' ')
                else:
                    print('?', end=' ')
            print()
