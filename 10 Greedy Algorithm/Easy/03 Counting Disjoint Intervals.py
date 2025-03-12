def count_disjoint_intervals(intervals):
    intervals = sorted(intervals, key=lambda x : x[1])

    prev_s, prev_e = intervals[0]
    count = 1

    for s, e in intervals:
        if s <= prev_e:
            pass
        else:
            prev_s, prev_e = s, e
            count += 1

    return count

intervals = [[0, 2], [2, 10], [4, 6]]
print(count_disjoint_intervals(intervals))