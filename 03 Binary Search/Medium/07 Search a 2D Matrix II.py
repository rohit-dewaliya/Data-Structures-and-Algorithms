def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])

    top, bottom = 0, m - 1
    left, right = 0, n - 1
    col = -1

    while left <= right:
        mid = (left + right) // 2
        if matrix[0][mid] < target < matrix[m - 1][mid]:
            print(matrix[0][mid], matrix[m - 1][mid])
            col = mid
            break
        elif matrix[0][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(col)

    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
result = search_2d_matrix(matrix, target)
print(result)
