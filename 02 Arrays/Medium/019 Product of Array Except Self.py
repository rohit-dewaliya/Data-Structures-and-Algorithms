def product_self(nums):
    n = len(nums)
    product_nums = [0] * n
    zeroes = nums.count(0)
    if zeroes >=2 :
        return product_nums
    product = 1
    index = None
    for num in nums:
        if num != 0:
            product *= num
        else:
            index = nums.index(num)

    if zeroes == 1:
        product_nums[index] = product
    else:
        for i in range(0, n):
            product_nums[i] = int(product / nums[i])

    return product_nums

nums = [1, 2, 0, 4, 5, 6, 0]
print(product_self(nums))
