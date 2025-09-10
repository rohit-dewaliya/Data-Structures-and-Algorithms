def humming_weight(n):
    num = 0

    while n > 0:
        if n & 1 == 1:
            num += 1
        n >>= 1

    return num


n = 11
print(humming_weight(n))