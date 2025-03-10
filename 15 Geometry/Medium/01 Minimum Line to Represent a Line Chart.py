from time_decorator import complexity_profiler


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


@complexity_profiler
def num_lines(stockPrices):
    n = len(stockPrices)
    if n < 2:
        return 0

    stockPrices.sort(key = lambda x : x[0])
    count = 1
    prev_slope = cal_slope(stockPrices[0], stockPrices[1])

    for i in range(1, n - 1):
        slope = cal_slope(stockPrices[i], stockPrices[i + 1])
        print(stockPrices[i], stockPrices[i + 1], slope, prev_slope)
        if slope != prev_slope:
            count += 1
            prev_slope = slope

    return count


stockPrices = [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]
print(num_lines(stockPrices))