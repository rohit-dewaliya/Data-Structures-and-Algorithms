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
        self.solve(0, 0)
        return self.board


board = [[".",".","4","7",".",".","3","2","."],
         [".",".",".","4","5",".",".",".","."],
         [".","8",".","1",".","3","6",".","."],
         ["4","3",".","5","6","7",".","9","."],
         [".",".",".",".",".",".",".",".","2"],
         ["1",".",".",".",".",".",".","6","."],
         [".",".","6",".",".",".","5",".","."],
         [".",".","3",".","7","8",".","1","."],
         ["2","1",".","3","4",".",".",".","."]]

Solution().solveSudoku(board)

for row in board:
    print(row)
