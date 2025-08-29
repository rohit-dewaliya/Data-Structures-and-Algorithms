def permutate(nums):
    result = []

    def bactrack(start):
        if start == len(nums):
            print(nums[:])
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            bactrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    bactrack(0)
    return result

nums = [1, 2, 3]
print("Final Result: ", permutate(nums))