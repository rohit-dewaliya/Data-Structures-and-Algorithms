def largest_number(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            num_1 = str(nums[i])
            num_2 = str(nums[j])
            if int(num_1 + num_2) < int(num_2 + num_1):
                nums[i], nums[j] = nums[j], nums[i]

    num = "".join(str(num) for num in nums)
    return str(int(num))


    nums = list(map(str, nums))        
    nums.sort(key=lambda x: x*10, reverse=True)
    if nums[0] == "0":
        return "0"
    largest = ''.join(nums)
    return largest


nums = [3, 30, 34, 5, 9]
print(largest_number(nums))
