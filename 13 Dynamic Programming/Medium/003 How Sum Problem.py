'''
def how_sum(target, nums, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums:
        remainder = target - num
        remainder_result = how_sum(remainder, nums, memo)
        if remainder_result != None:
            memo[target] = remainder_result + [num]
            return memo[target]
    memo[target] = None
    return memo[target]
'''


# Using Tabulation-------------------------------#
def is_subset_sum(target, nums):
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target + 1):
        if table[i] is not None:
            for num in nums:
                if i + num <= target and table[i + num] is None:
                    table[i + num] = table[i] + [num]

    return table[target]


# Using Memoization---------------------------------#
# def is_subset_sum(target, nums, memo = {}):
#     if target in memo:
#         return memo[target]
#     if target == 0:
#         return True
#     if target < 0:
#         return False
#
#     for i in range(len(nums)):
#         remainder = target - nums[i]
#         popped_element = nums.pop(i)
#         remainder_result = is_subset_sum(nums, remainder, memo)
#         nums.insert(i, popped_element)
#         if remainder_result:
#             memo[remainder] = True
#             return True
#
#     memo[target] = False
#     return False


nums = [5, 4, 3]
target = 70
print(is_subset_sum(target, nums))