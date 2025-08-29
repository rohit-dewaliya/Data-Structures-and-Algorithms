class Solution:
    def minimumRemovals(self, nums, k):
        nums.sort()
        n = len(nums)
        max_len = 0
        left = 0

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len

print(Solution().minimumRemovals([1, 34, 23], 2))  # Output: 1

'''
class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1

        while right >= 0:
            if nums[right] <= nums[left] * k:
                return n - right - 1
            else:
                right -= 1

        return 1

nums = [25]
k = 1
print(Solution().minRemoval(nums, k))
'''
