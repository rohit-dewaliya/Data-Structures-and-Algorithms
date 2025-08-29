from itertools import groupby


class Solution:
    def longestSubarray(self, nums):
        # METHOD I----------------------------------------------#
        # highest = max(nums)
        #
        # max_count = 0
        # count = 0
        #
        # for i in range(len(nums)):
        #     if nums[i] == highest and nums[i - 1] != highest:
        #         count += 1
        #
        #     if nums[i] == highest and nums[i - 1] == highest:
        #         count += 1
        #
        #     if nums[i] != highest:
        #         count = 0
        #
        #     max_count = max(max_count, count)
        # return max_count


        # METHOD II----------------------------------------------#
        highest = max(nums)

        return max(len(list(values)) for key, values in groupby(nums) if key == highest)

nums = [1, 2, 3, 4]
sol = Solution()
result = sol.longestSubarray(nums)
print(result)