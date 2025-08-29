# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
def max_tiplet(nums):
    n = len(nums)
    maximum = 0
    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            

nums = [12, 6, 1, 2, 7]
result = max_tiplet(nums)
print(result)