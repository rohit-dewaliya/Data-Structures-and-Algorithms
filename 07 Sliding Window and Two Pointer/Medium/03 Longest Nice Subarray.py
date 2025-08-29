class Solution:
    def longestNiceSubarray(self, nums):
        n = len(nums)
        left = 0
        max_len = 0
        bitmask = 0

        for right in range(0, n):
            while bitmask & nums[right] != 0:
                bitmask ^= nums[left]
                left += 1

            bitmask |= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len

nums = [3,1,5,11,13]
sol = Solution()
result = sol.longestNiceSubarray(nums)
print(result)
