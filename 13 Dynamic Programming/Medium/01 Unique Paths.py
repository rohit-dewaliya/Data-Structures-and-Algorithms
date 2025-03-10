from time_decorator import complexity_profiler

# Using Tabulization-----------------#
def unique_path(m, n):
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    table[1][1] = 1

    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if j < n:
                table[i][j + 1] += table[i][j]
            if i < m:
                table[i + 1][j] += table[i][j]
    return table[m][n]

# Using Memoization---------------#
memo = {}
def unique_paths(m, n):
    key = (m, n)
    if key in memo:
        return memo[key]

    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1

    memo[key] = unique_paths(m - 1, n) + unique_paths(m, n - 1)
    return memo[key]

m = 18
n = 18
print(unique_path(m, n))  # Expected Output: 3
