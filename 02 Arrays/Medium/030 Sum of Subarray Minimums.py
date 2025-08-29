def sum_subarray(arr):
    total = 0
    _min = float('inf')
    result = []

    def backtrack(start, path):
        nonlocal total, _min
        if path:
            total += _min
            result.append(path[:])

        if start < len(arr):
            _min = min(_min, arr[start])
            backtrack(start + 1, path + [arr[start]])

    for i in range(len(arr)):
        backtrack(i, [])
        _min = float('inf')

    return total

arr = [11,81,94,43,3]
print(sum_subarray(arr))