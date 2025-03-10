def longest_consecutive_sequenc(nums):
    n = len(nums)
    if n <= 1:
        return n

    nums.sort()
    max_consecutive = 1
    temp_consecutive = 1

    for i in range(1, n):
        # print(i, nums[i], temp_consecutive, max_consecutive)
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] == nums[i - 1] + 1:
            temp_consecutive += 1
            max_consecutive = max_consecutive if max_consecutive >= temp_consecutive else temp_consecutive
        elif nums[i] != nums[i - 1] + 1:
            temp_consecutive = 1

    return max_consecutive


nums = [0, 0, 1, 5, 4, 3, 8, 7, 5, 2, 6, 2, 5, 7, 4, 4, 6, 45, 23, 65]
print(longest_consecutive_sequenc(nums))
