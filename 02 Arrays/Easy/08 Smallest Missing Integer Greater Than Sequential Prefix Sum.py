def missing_integer(nums):
    num = 0
    n = len(nums)
    consecutive = [0] * n
    consecutive[0] = 1

    for i in range(1, n):
        if nums[i - 1] == nums[i] - 1:
            consecutive[i] = 1

    print(consecutive, nums)
    total = 0
    for i in range(0, n):
        print(i, total, num)
        if consecutive[i] == 1:
            num += nums[i]
        else:
            num = 0
        total = max(total, nums[i])
    return num

nums = [1, 2, 3, 2, 5]
result = missing_integer(nums)
print(result)