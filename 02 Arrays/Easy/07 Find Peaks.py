def find_peaks(mountain):
    peaks = []
    for i in range(1, len(mountain) - 1):
        if mountain[i - 1] < mountain[i] > mountain[i + 1]:
            peaks.append(i)

    return peaks

mountain = [1,4,3,8,5]
result = find_peaks(mountain)
print(result)