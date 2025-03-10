def sub_array_sum(nums, k):
    n = len(nums)
    count = 0
    prefix_sum = {0: 1}
    _sum = 0

    for i in range(n):
        _sum += nums[i]
        diff = _sum - k
        count += prefix_sum.get(diff, 0)
        prefix_sum[_sum] = prefix_sum.setdefault(_sum, 0) + 1

    return count

nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 9
print(sub_array_sum(nums, k))
