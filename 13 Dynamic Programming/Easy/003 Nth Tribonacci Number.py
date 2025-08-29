class Solution:
    def __init__(self):
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n <= 0:
            return 0
        elif n < 3:
            return 1

        self.memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.memo[n]

n = 37

solution = Solution()
result = solution.tribonacci(n)
print(result)