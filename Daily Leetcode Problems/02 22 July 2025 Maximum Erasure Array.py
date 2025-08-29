def maximum_erasure_array(nums):
    n = len(nums)
    num_set = set()
    left = 0
    _sum = 0
    max_sum = 0

    for right in range(n):
        while nums[right] in num_set:
            num_set.remove(nums[left])
            _sum -= nums[left]
            left += 1
        num_set.add(nums[right])
        _sum += nums[right]
        max_sum = max(max_sum, _sum)

    return max_sum

nums = [5,2,1,2,5,2,1,2,5]
result = maximum_erasure_array(nums)
print(result)
