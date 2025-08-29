def zero_filled(nums):
    n = len(nums)
    count = 0
    left = 0

    while left < n:
        if nums[left] == 0:
            right = left
            while right < n and nums[right] == 0:
                right += 1
            m = right - left
            count += (m * (m + 1)) // 2
            left = right
        else:
            left += 1
    return count

nums = [1, 2, 0, 0, 3, 0, 0]
print(zero_filled(nums))
