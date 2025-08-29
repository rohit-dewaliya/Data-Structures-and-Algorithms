def isPowerOfTwo(n):
    # Method I-------------------------------#
    # return n > 0 and n & (n - 1) == 0

    # Method II-------------------------------#
    if n < 1:
        return False
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1

    return count == 1

n = 48
print(isPowerOfTwo(n))