def max_area(dimensions):
    # METHOD I-----------------------------#
    # def calculate_diagonal(w, h):
    #     x = w ** 2 + h ** 2
    #     return x ** 0.5
    #
    # for i in range(0, len(dimensions)):
    #     dimensions[i].append(calculate_diagonal(dimensions[i][0], dimensions[i][1]))
    #
    # dimensions = sorted(dimensions, key=lambda x: x[2], reverse=True)
    #
    # diagonal = dimensions[0][2]
    # highest_area = dimensions[0][0] * dimensions[0][1]
    #
    # for d in range(1, len(dimensions)):
    #     if diagonal == dimensions[d][2]:
    #         highest_area = max(highest_area, dimensions[d][0] * dimensions[d][1])
    #     else:
    #         break
    #
    # return highest_area

    # METHOD II-------------------------------#
    max_diagonal = 0
    max_area = 0

    for w, h in dimensions:
        diag_sq = w * w + h * h
        area = w * h

        if diag_sq > max_diagonal:
            max_diagonal = diag_sq
            max_area = area
        elif diag_sq == max_diagonal:
            max_area = max(max_area, area)

    return max_area

dimensions = [[9,3],[8,6]]
print(max_area(dimensions))