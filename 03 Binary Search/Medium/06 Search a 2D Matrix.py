def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])

    top, bottom = 0, m - 1
    row = -1
    while top <= bottom:
        mid = (top + bottom) // 2
        if matrix[mid][0] <= target <= matrix[mid][n - 1]:
            row = mid
            break
        elif target < matrix[mid][0]:
            bottom = mid - 1
        else:
            top = mid + 1

    if row == -1:
        return False

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result = search_2d_matrix(matrix, target)
print(result)
