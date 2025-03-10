def merge_intervals(intervals):
    n = len(intervals)
    if n <= 1:
        return intervals

    intervals.sort(key = lambda x : x[0])

    merged_intervals = [intervals[0]]

    for i in range(1, n):
        prev = merged_intervals[-1]
        curr = intervals[i]

        if prev[1] >= curr[0]:
            prev[1] = max(prev[1], curr[1])
        else:
            merged_intervals.append(curr)

    return merged_intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))