def three_closest_sum(nums, target):
    nums.sort()
    n = len(nums)
    closest = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            _sum = nums[i] + nums[left] + nums[right]

            if abs(target - _sum) < abs(target - closest):
                closest = _sum

            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                return _sum

    return closest

nums = [-1, 2, 1, -4]
target = 1
result = three_closest_sum(nums, target)
print(result)