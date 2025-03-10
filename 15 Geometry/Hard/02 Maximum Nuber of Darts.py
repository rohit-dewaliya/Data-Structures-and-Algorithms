from time_decorator import complexity_profiler

def cal_distances(point):
    y = (point[1] ** 2) ** 0.5
    x = (point[0] ** 2) ** 0.5

    return y + x

@complexity_profiler
def maximum_darts(darts, r):
    n = len(darts)
    max_darts = 0

    for dart in darts:
        distance = cal_distances(dart)
        print(dart, ' - ', distance)
        if distance < r:
            max_darts += 1

    return max_darts


darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]]
r = 5
maximum_darts(darts, r)
