def minimum_bit_flip(start, goal):
    c = start ^ goal
    count = 0
    while c > 0:
        if c & 1:
            count += 1
        c = c >> 1

    return count

start= 3
goal = 4
res = minimum_bit_flip(start, goal)
print(res)