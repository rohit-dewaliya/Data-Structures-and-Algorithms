def max_product_subarray(nums):
    prod1, prod2 = nums[0], nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod1 = temp
        result = max(result, prod1)
    return result
'''
    n = len(nums)
    max_product = float('-inf')
    prefix, suffix = 1, 1
    for i in range(0, n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[n - i - 1]
        max_product = max(max_product, max(prefix, suffix))

    return max_product
'''

nums = [2, 3, -2, 4]
print(max_product_subarray(nums))