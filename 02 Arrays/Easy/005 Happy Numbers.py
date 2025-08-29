def happy_numbers(n):
    def get_nums(n):
        nums = []
        while n > 0:
            res = n % 10
            nums.append(res)
            n = n // 10

        return nums

    def get_sum(nums):
        sum = 0
        for num in nums:
            sum += num ** 2

        return sum

    while True:
        nums = get_nums(n)
        n = get_sum(nums)
        if n == 1 or n == 7:
            return True
        if n < 10:
            return False


n = 1111111
print(happy_numbers(n))