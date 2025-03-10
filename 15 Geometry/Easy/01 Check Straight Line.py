from time_decorator import complexity_profiler


def cal_gcd(a, b):
    if b == 0:
        return a
    return cal_gcd(b, a % b)

def check_slope(coordinate1, coordinate2):
    y = coordinate2[1] - coordinate1[1]
    x = coordinate2[0] - coordinate1[0]

    if x == 0:
        return float('inf')

    return y / x

@complexity_profiler
def check_straight_line(coordinates):
    slope = check_slope(coordinates[0], coordinates[1])

    for i in range(2, len(coordinates)):
        temp_slope = check_slope(coordinates[i - 1], coordinates[i])

        if temp_slope != slope:
            return False

    return True

coordinates = [[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]
check_straight_line(coordinates)
