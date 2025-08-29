def max_sum(nums):
    m = max(nums)
    if m < 0:
        return m

    nums = set(nums)
    _sum = 0
    for num in nums:
        if num >= 0:
            _sum += num

    return _sum

nums = [-3,-3,-3,0]
result = max_sum(nums)
print(result)
