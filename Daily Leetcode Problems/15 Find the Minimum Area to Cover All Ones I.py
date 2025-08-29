def minimum_area(grid):
    width = [float('inf'), float('-inf')]
    height = [float('inf'), float('-inf')]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                width[0] = min(width[0], row)
                height[0] = min(height[0], col)
                width[1] = max(width[1], row)
                height[1] = max(height[1], col)

    return int(width[1] - width[0] + 1) * int(height[1] - height[0] + 1)


grid = [[0],[1]]
result = minimum_area(grid)
print(result)