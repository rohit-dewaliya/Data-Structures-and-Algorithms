def sum_of_subarray_ranges(nums):
    total = 0

    def backtrack(start, path):
        nonlocal total
        if path:
            total += max(path) - min(path)

        if start < len(nums):
            backtrack(start + 1, path + [nums[start]])

    for i in range(len(nums)):
        backtrack(i, [])

    return total


nums = [1, 2, 3]
print("Sum of subarray ranges:", sum_of_subarray_ranges(nums))
