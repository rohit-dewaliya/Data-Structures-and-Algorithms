def find_ways(points):
    count = 0
    points = sorted(points, key = lambda x : x[0])
    return count

points = [
    [[1,1],[2,2],[3,3]],
    [[6,2],[4,4],[2,6]],
    [[3,1],[1,3],[1,1]],
]
for point in points:
    result = find_ways(point)
    print(f"Testcase {points.index(point) + 1}:", result)