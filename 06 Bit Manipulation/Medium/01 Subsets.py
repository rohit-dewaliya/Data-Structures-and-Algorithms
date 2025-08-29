def subsets(nums):
    # n = len(nums)
    # _len = 2 ** n
    # power_set = []
    #
    # for i in range(_len):
    #     subset = []
    #     count = 0
    #     while i > 0:
    #         if i & 1:
    #             subset.append(nums[count])
    #         i >>= 1
    #         count += 1
    #
    #     power_set.append(subset)
    #
    # return power_set

    # Method II----------------------------------#
    power_set = []

    def backtrack(i, num):
        if i == len(nums):
            power_set.append(num[:])
            return

        backtrack(i + 1, num)

        num.append(nums[i])
        backtrack(i + 1, num)
        num.pop()


    backtrack(0, [])
    return power_set

nums = [1, 2, 3]
print(subsets(nums))