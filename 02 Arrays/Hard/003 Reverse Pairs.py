def reverse_pairs(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        j = n - 1
        while i < j:
            if nums[i] > 2 * nums[j]:
                count += 1
            j -= 1
    return count

nums = [2, 4, 3, 5, 1]
print(reverse_pairs(nums))