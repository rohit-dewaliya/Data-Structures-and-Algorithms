class Solution:
    def find_paths(self, m, n, grid, memo):
        key = (m, n)
        if key in memo:
            return memo[key]

        if m == 0 or n == 0:
            return 0
        if grid[m][n] == 1:
            return 0
        if m == 1 or n == 1:
            return 1

        memo[key] = self.find_paths(m - 1, n, grid, memo) + self.find_paths(m, n - 1, grid, memo)

        return memo[key]

    def uniquePathsWithObstacles(self, obstacleGrid):
        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 and n == 1:
            return 1
        return self.find_paths(m - 1, n - 1, obstacleGrid, memo)



obstacleGrid = [[0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))