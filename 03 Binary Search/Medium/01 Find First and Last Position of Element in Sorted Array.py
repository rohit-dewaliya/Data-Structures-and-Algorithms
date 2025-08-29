def search_range(nums, target):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            index = mid
            break
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if index == -1:
        return [-1, -1]

    start, end = index, index
    while start > 0 and nums[start - 1] == target:
        start -= 1
    while end < len(nums) - 1 and nums[end + 1] == target:
        end += 1

    return [start, end]

nums = [1, 2, 3 , 5, 8, 8, 8, 8]
target = 8
result = search_range(nums, target)
print(result)
