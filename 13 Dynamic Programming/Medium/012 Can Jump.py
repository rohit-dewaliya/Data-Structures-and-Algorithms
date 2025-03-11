# Using Tabulization-------------------#
def can_jump(nums):
    n = len(nums)
    table = [False for _ in range(n)]
    table[0] = True

    for i in range(0, n - 1):
        if i < n and table[i]:
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    table[i + j] = True

    return table[-1]

# Using Memoization---------------------#
class Solution:
    def jump(self, nums, i, memo):
        if i in memo:
            return memo[i]

        if i >= len(nums) - 1:
            return True
        if nums[i] == 0:
            return False

        for index in range(nums[i], 0, -1):
            if self.jump(nums, i + index, memo):
                memo[i] = True
                return True

        memo[i] = False
        return False

    def canJump(self, nums):
        memo = {}
        return self.jump(nums, 0, memo)


nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
(print(can_jump(nums)))

'''
Best Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
'''