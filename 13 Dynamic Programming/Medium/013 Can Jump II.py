def jump(nums):
    n = len(nums)
    table = [float("inf")] * n
    table[0] = 0

    for i in range(n):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                table[i + j] = min(table[i + j], table[i] + 1)

    return table[-1]

def jump_optimal(nums):
    n = len(nums)
    farthest = 0
    step = 0
    end = 0

    for i in range(0, n - 1):
        farthest = max(farthest, nums[i] + i)

        if i == end:
            step += 1
            end = farthest

    return step


nums = [3, 2, 0, 1, 4]
print(jump(nums))
print(jump_optimal(nums))