# def rob_helper(nums, index, memo={}):
#     if index in memo:
#         return memo[index]
#     if index >= len(nums):
#         return 0
#
#     rob_current = nums[index] + rob_helper(nums, index + 2, memo)
#     skip_current = rob_helper(nums, index + 1, memo)
#     memo[index] = max(rob_current, skip_current)
#
#     return memo[index]
#
# def rob(nums):
#     memo = {}
#     return rob_helper(nums, 0, memo)

def rob(self, nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]

nums = [2, 7, 9, 3, 1]
print(rob(nums))