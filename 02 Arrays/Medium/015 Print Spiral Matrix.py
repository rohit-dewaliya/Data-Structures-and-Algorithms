def print_spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    spiral = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # Moving to Right
        for i in range(left, right):
            spiral.append(matrix[top][i])
        top += 1

        # Moving Down
        for i in range(top, bottom):
            spiral.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # Moving to Left
        for i in range(right - 1, left - 1, -1):
            spiral.append(matrix[bottom - 1][i])
        bottom -= 1

        # Moving Up
        for i in range(bottom - 1, top - 1, -1):
            spiral.append(matrix[i][left])
        left += 1

    return spiral


# Test Case
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

print(print_spiral_matrix(matrix))
