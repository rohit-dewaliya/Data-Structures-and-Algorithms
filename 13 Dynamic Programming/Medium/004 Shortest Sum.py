# Using Tabulation-------------------------------#
def shortest_sum(target, nums):
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target + 1):
        if table[i] is not None:
            for num in nums:
                if i + num <= target and table[i + num] is None:
                    combination = table[i] + [num]
                    if table[i + num] == None or len(table[i + num]) > len(combination):
                        table[i + num] = combination

    return table[target]


# Using Memoization---------------------------------#
# def shortest_sum(target, nums, memo = {}):
#     if target in memo:
#         return memo[target]
#
#     if target == 0:
#         return []
#
#     if target < 0:
#         return None
#
#     shortest_nums = None
#
#     for num in nums:
#         remainder = target - num
#         remainder_result = shortest_sum(nums, remainder)
#         if remainder_result != None:
#             remainder_result = remainder_result + [num]
#             if shortest_nums == None or (len(remainder_result) < len(shortest_nums)):
#                 shortest_nums = remainder_result
#
#     memo[target] = shortest_nums
#     return shortest_nums


nums = [2, 3, 5, 6]
target = 200
print(shortest_sum(target, nums))