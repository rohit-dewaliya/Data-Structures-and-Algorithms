from xml.etree.ElementTree import register_namespace


def count_hills_valleys(nums):
    n = len(nums)
    result = 0
    new_nums = [nums[0]]
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            new_nums.append(nums[i])

    n = len(new_nums)
    for i in range(1, n - 1):
        if new_nums[i - 1] < new_nums[i] and new_nums[i] > new_nums[i + 1]:
            result += 1
        elif new_nums[i - 1] > new_nums[i] and new_nums[i] < new_nums[i + 1]:
            result += 1

    return new_nums, result


num = [6, 6, 5, 5, 4, 1]
result = count_hills_valleys(num)
print(result)