def minimum_falling_path(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(1, m):
        for j in range(0, n):
            if j == 0:
                matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1])
            elif j == n - 1:
                matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j - 1])
            else:
                matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])
    return min(matrix[-1])

matrix = [[-19, 57], [-40, -5]]
print(minimum_falling_path(matrix))