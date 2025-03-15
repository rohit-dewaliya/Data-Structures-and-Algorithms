from typing import List


class Solution:
    def search(self, board, target, i, j):
        if not target:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != target[0]:
            return False

        temp = board[i][j]
        board[i][j] = "*"

        found = (
                self.search(board, target[1:], i - 1, j) or
                self.search(board, target[1:], i + 1, j) or
                self.search(board, target[1:], i, j - 1) or
                self.search(board, target[1:], i, j + 1)
        )

        board[i][j] = temp
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCEDF"
print(Solution().exist(board, word))