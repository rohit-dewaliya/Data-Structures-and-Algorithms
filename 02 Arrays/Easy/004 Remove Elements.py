def remove_elements(nums, val):
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        if nums[left] == val and nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        if nums[left] != val:
            left += 1
        if nums[right] == val:
            right -= 1

    for num in nums:
        if num == val:
            break
        count += 1

    return count, nums

nums = [2]
val = 2
result = remove_elements(nums, val)
print(result)