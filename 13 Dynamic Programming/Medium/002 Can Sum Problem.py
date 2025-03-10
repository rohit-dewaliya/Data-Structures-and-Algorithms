# Using Tabulation-------------------------------#
def can_sum(target, nums):
    table = [False] * (target + 1)
    table[0] = True

    for i in range(0, target + 1):
        if table[i]:
            for num in nums:
                if num + i <= target:
                    table[i + num] = True
    return table[target]

# Using Memoization---------------------------------#
count = 0
# def can_sum(target, nums, count = 0):
# def can_sum(target, nums, memo = {}):
#     if target in memo:
#         return memo[target]
#
#     if target == 0:
#         return True
#
#     if target < 0:
#         return False
#
#     for num in nums:
#         remainder = target - num
#         if can_sum(remainder, nums, memo):
#             memo[remainder] = True
#             return True
#         # if can_sum(remainder, nums, count):
#             # count += 1
#     # return count
#     return False

target = 110000
nums = [5, 3, 4, 7]
print(can_sum(target, nums))