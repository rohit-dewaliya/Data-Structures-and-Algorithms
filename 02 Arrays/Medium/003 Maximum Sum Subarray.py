def maximum_sum(nums):
    max_sum = float('-inf')
    curr_sum = 0

    for i in range(0, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)

    return max_sum

nums = [5,4,-1,7,8]
print(maximum_sum(nums))