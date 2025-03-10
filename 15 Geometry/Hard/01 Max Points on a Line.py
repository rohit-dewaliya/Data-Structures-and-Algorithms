from time_decorator import complexity_profiler

def check_slope(coordinate1, coordinate2):
    y = coordinate2[1] - coordinate1[1]
    x = coordinate2[0] - coordinate1[0]

    if x == 0:
        return float('inf')

    return y / x

@complexity_profiler
def max_points(points):
    n = len(points)
    max_number_points = 0

    for i in range(0, n):
        point = points[i]
        freq = {}
        for j in range(i + 1, n):
            slope = check_slope(point, points[j])
            freq[slope] = freq.setdefault(slope, 0) + 1

        if freq != {}:
            temp_max = max(freq.values())
            max_number_points = max(max_number_points, temp_max)

    return max_number_points + 1


points = [[0,0],[1073741822,2147483645],[1073741823,2147483647]]
max_points(points)
