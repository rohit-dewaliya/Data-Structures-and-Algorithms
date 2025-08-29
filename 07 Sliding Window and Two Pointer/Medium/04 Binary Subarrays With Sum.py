class Solution:
    def numSubarraysWithSum(self, nums, goal):
        prefix_sum = {0 : 1}
        _sum = 0
        result = 0

        for num in nums:
            _sum += num

            remainder = _sum - goal
            
            result += prefix_sum.get(remainder, 0)
            prefix_sum[_sum] = prefix_sum.get(_sum, 0) + 1
            

        return result
                


nums = [0, 0, 0, 0, 0]
goal = 0
sol = Solution()
result = sol.numSubarraysWithSum(nums, goal)
print(result)
