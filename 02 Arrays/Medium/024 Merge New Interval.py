def merge_interval(intervals, newInterval):
    # METHOD I--------------------------------------#
    # intervals.append(newInterval)
    #
    # n = len(intervals)
    #
    # if n <= 1:
    #     return intervals
    #
    # intervals.sort(key = lambda x: x[0])
    #
    # merged_intervals = [intervals[0]]
    #
    # for i in range(1, n):
    #     prev = merged_intervals[-1]
    #     curr = intervals[i]
    #
    #     if prev[1] >= curr[0]:
    #         prev[1] = max(prev[1], curr[1])
    #     else:
    #         merged_intervals.append(curr)
    #
    # return merged_intervals

    # METHOD II--------------------------------------#
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last = merged_intervals[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged_intervals.append(current)

    return merged_intervals


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4,8]

result = merge_interval(intervals, newInterval)
print(result)