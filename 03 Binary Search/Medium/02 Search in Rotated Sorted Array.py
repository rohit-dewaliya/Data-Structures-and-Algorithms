def search_rotated(nums, target):
    def find_pivot(nums):
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return 0

        while left <= right:
            mid = (left + right) // 2
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return 0

    def binary_search(nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    n = len(nums)
    if n == 0:
        return -1

    pivot = find_pivot(nums)

    if nums[pivot] <= target <= nums[n - 1]:
        return binary_search(nums, pivot, n - 1, target)
    else:
        return binary_search(nums, 0, pivot - 1, target)


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated(nums, target))
