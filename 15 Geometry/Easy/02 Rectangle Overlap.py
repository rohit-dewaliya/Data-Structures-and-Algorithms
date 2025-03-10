from time_decorator import complexity_profiler


@complexity_profiler
def rectangle_overlap(rec1, rec2):
    x1, y1, x2, y2 = rec1
    m1, n1, m2, n2 = rec2

    if x2 <= m1 or m2 <= x1 or y2 <= n1 or n2 <= y1:
        return False

    return True

rect1 = [2, 17, 6, 20]
rect2 = [3, 8, 6, 20]
rectangle_overlap(rect1, rect2)