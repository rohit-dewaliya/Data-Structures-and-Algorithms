def reordered_power_of_2(n):
    # Method I---------------------------#
    # def num_to_array(n):
    #     nums = []
    #     while n > 0:
    #         nums.append(n % 10)
    #         n = n // 10
    #     nums.reverse()
    #     return nums
    #
    # def array_to_nums(nums):
    #     n = 0
    #     for num in nums:
    #         n = n * 10 + num
    #     return n
    #
    # def bactrack(start):
    #     if start == len(nums):
    #         num = array_to_nums(nums[:])
    #         return num > 0 and num & (num - 1) == 0
    #
    #     for i in range(start, len(nums)):
    #         if start == 0 and nums[i] == 0:
    #             continue
    #         nums[start], nums[i] = nums[i], nums[start]
    #         if bactrack(start + 1):
    #             return True
    #         nums[start], nums[i] = nums[i], nums[start]
    #
    #     return False
    #
    # nums = num_to_array(n)
    #
    # return bactrack(0)

    # Method II---------------------------#
    def count_digits(x):
        return "".join(sorted(str(x)))

    target = count_digits(n)
    for i in range(31):
        if count_digits(i) == target:
            return True

    return False

n = 106
print("Final Result: ", reordered_power_of_2(n))