import time

class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        left = 0
        max_ones = 0
        zero_count = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)

        return max_ones


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

sol = Solution()
result = sol.longestOnes(nums, k)
print(result)
