def minimum_suffix_flips(target):
    n = len(target)
    count = 0
    index = 0
    while index < n and target[index] != '1':
        index += 1

    for i in range(index, n):
        if i > 0 and target[i] != target[i - 1]:
            count += 1

    if target[0] == '1':
        count += 1

    return count

def min_suffix_flips(target):
    count = 0
    last = '0'

    for bit in target:
        if bit != last:
            count += 1
            last = bit

    return count

target = '101'
print(minimum_suffix_flips(target))
print(min_suffix_flips(target))