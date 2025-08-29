def single_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return nums[left]

nums = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
print(single_element(nums))