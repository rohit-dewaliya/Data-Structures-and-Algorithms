def longest_subarray(arr, k):
    n = len(arr)
    presum_map = {}
    _sum = 0
    max_length = 0

    for i in range(n):
        _sum += arr[i]

        if _sum == k:
            max_length = max(max_length, i + 1)

        remainder = _sum - k

        if remainder in presum_map:
            max_length = max(max_length, i - presum_map[remainder])

        if _sum not in presum_map:
            presum_map[_sum] = i

    return max_length

arr = [2, 0, 0, 3]
k = 5
print(longest_subarray(arr, k))