def missing_repeated_nums(grid):
    n = len(grid)
    missing = None
    repeated = None
    max_num = n * n
    real_sum = 0
    freq = set()
    for i in range(n):
        for j in range(n):
            real_sum += grid[i][j]
            if grid[i][j] in freq:
                repeated = grid[i][j]
            freq.add(grid[i][j])
    actual_sum = (max_num * (max_num + 1)) / 2
    missing = int(actual_sum - (real_sum - repeated))
    return repeated, missing


grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print(missing_repeated_nums(grid))