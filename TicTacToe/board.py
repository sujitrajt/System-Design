class Board:
    def __init__(self):
        self.grid  = [['-' for _ in range(3)] for _ in range(3)]
        self.moves_count = 0

    def make_move(self, rows,cols,symbol):
        if not(0 <=rows<=3 and 0<=cols<=3) and self.grid[rows][cols] != "-":
            raise ValueError("Invalid move")
        self.grid[rows][cols] = symbol
        self.moves_count += 1

    def is_full(self):
        return self.moves_count == 9
    
    def is_winner(self):
        for row in range(3):
            if self.grid[row][0] != "-" and self.grid[row][0] == self.grid[row][1] == self.grid[row][2]:
                return True
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != "-":
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]and self.grid[0][0] != "-":
            return True
        return self.grid[0][2] == self.grid[1][1] == self.grid[2][0]and self.grid[0][2] != "-"
    
    def print_board(self):
        for row in self.grid:
            print(" ".join(row))
        print("\n")
