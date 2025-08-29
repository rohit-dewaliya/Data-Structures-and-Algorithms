def next_greater(nums1, nums2):
    stack = []
    next_greater_num = {}

    for num in nums2:
        while stack and num > stack[-1]:
            next_greater_num[stack.pop()] = num
        stack.append(num)

    while stack:
        next_greater_num[stack.pop()] = -1

    return [next_greater_num[num] for num in nums1]
    # m, n = len(nums1), len(nums2)
    # greater = []
    #
    # index_map = {value : index for index, value in enumerate(nums2)}
    #
    # for i in range(m):
    #     index = index_map[nums1[i]]
    #
    #     great = -1
    #
    #     for j in range(index + 1, n):
    #         if nums1[i] < nums2[j]:
    #             great = nums2[j]
    #             break
    #
    #     greater.append(great)
    #
    # return greater

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater(nums1, nums2))