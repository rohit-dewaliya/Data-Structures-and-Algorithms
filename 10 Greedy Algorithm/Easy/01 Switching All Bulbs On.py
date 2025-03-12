def switching_bulbs(bulbs):
    cost = 0

    for b in bulbs:
        if cost % 2 == 0:
            b = b
        else:
            b = not b

        if b % 2 == 1:
            continue
        else:
            cost += 1

    return cost

# 001011101
bulbs = [0, 0, 1, 0, 1, 1, 1, 0, 1]
print(switching_bulbs(bulbs))