from time_decorator import complexity_profiler

@complexity_profiler
def partion_pivot(nums, pivot):
    n = len(nums)
    partioned_nums = []
    left_partion = []
    pivot_nums = []
    right_nums = []

    for num in nums:
        if num < pivot:
            left_partion.append(num)
        elif num == pivot:
            pivot_nums.append(pivot)
        else:
            right_nums.append(num)

    return left_partion + pivot_nums + right_nums

nums = [9,12,5,10,14,3,10]
pivot = 10
partion_pivot(nums, pivot)