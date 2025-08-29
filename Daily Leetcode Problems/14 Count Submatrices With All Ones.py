def count_submatrices(mat):
    m, n = len(mat), len(mat[0])
    dp = [[0] * n for _ in range(m)]
    total = 0

    for i in range(m):
        for j in range(n):
            if mat[i][j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]
                total += dp[i][j]

    return total

mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
print(count_submatrices(mat))