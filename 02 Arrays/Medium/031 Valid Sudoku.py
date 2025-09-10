class Solution:
    def __init__(self):
        self.board = None

    def is_valid(self, row, col, num):
        num = str(num)
        block_row = (row // 3) * 3
        block_col = (col // 3) * 3

        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
            if self.board[block_row + i // 3][block_col + i % 3] == num:
                return False
        return True

    def solve(self, row, col):
        if row == 8 and col == 9:
            return True

        if col == 9:
            row += 1
            col = 0

        if self.board[row][col] != ".":
            return self.solve(row, col + 1)

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = str(num)
                if self.solve(row, col + 1):
                    return True
                self.board[row][col] = "."

        return False

    def solveSudoku(self, board):
        self.board = board
        return self.solve(0, 0)


board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
Solution().solveSudoku(board)

for row in board:
    print(row)
