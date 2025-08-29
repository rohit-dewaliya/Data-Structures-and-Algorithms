def next_greater_element(n):
    nums = list(map(int, str(n)))
    _len = len(nums)

    i = _len - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = _len - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = reversed(nums[i + 1:])

    result = int("".join(map(str, nums)))

    return result if result > n else -1


n = 124651
print(next_greater_element(n))
