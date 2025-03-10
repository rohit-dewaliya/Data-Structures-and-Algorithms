from time_decorator import complexity_profiler

@complexity_profiler
def four_sum(nums, target):
    n = len(nums)
    result = []
    nums.sort()

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k, m = j + 1, n - 1
            while k < m:
                _sum = nums[i] + nums[j] + nums[k] + nums[m]

                if _sum > target:
                    m -= 1
                elif _sum < target:
                    k += 1
                else:
                    result.append([nums[i], nums[j], nums[k], nums[m]])

                    while k < m and nums[k] == nums[k + 1]:
                        k += 1
                    while k < m and nums[m] == nums[m - 1]:
                        m -= 1

                    k += 1
                    m -= 1

    return result

nums = [-2, -1, -1, 1, 1, 2, 2]
target = 0
print(four_sum(nums, target))