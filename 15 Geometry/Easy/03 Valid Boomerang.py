def valid_boomerang(points):
    def cal_gcd(a, b):
        if b == 0:
            return a
        return cal_gcd(b, a % b)


    def cal_slope(point1, point2):
        y = point2[1] - point1[1]
        x = point2[0] - point1[0]

        if x == 0:
            return (1, 0)

        gcd = cal_gcd(abs(y), abs(x))
        y //= gcd
        x //= gcd

        if x < 0:
            y = -y
            x = -x

        return (y, x)

    if points[0] == points[1] or points[1] == points[2] or points[2] == points[1]:
        return False

    slope_1 = cal_slope(points[0], points[1])
    slope_2 = cal_slope(points[1], points[2])

    return not slope_1 == slope_2

points = [[1, 1], [2, 2], [3, 3]]
print(valid_boomerang(points))
