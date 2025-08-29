def k_closet_origin(points, k):
    result_points = []

    def distance(point):
        x_dis = point[0] ** 2
        y_dis = point[1] ** 2

        return x_dis + y_dis

    for point in points:
        dis = distance(point)
        point.append(dis)

    points = sorted(points, key = lambda x: x[2])

    for i in range(0, k):
        result_points.append([points[i][0], points[i][1]])

    return result_points


points = [[3,3],[5,-1],[-2,4]]
k = 2
result = k_closet_origin(points, k)
print(result)
