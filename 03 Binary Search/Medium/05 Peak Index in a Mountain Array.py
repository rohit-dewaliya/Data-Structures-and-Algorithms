def peak_index(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
 
arr = [0, 1, 0]
result = peak_index(arr)
print(result)