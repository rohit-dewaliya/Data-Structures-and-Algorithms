def general_spiral_matrix(n):
    if n == 1:
        return [[1]]

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    count = 1

    while left < right and top < bottom:
        # Moving to Right
        for i in range(left, right):
            matrix[top][i] = count
            count += 1
        top += 1

        # Moving Down
        for i in range(top, bottom):
            matrix[i][right - 1] = count
            count += 1
        right -= 1

        if not (left < right and top < bottom):
            break

        # Moving to Left
        for i in range(right - 1, left - 1, -1):
            matrix[bottom - 1][i] = count
            count += 1
        bottom -= 1

        # Moving Up
        for i in range(bottom - 1, top - 1, -1):
            matrix[i][left] = count
            count += 1
        left += 1

    return matrix


n = 10
print(general_spiral_matrix(n))
