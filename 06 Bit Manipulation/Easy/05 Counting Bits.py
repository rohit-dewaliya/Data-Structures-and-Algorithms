def counting_bits(n):
    # Method I----------------------------#
    count = [0] * (n + 1)
    for i in range(0, n + 1):
        num = i
        while num > 0:
            if num & 1 == 1:
                count[i] += 1
            num >>= 1

    return count
    # Method II-----------------------------#
    # dp = [0] * (n + 1)
    # offset = 1
    # for i in range(1, n + 1):
    #     if offset * 2 == i:
    #         offset = i
    #     dp[i] = 1 + dp[i - offset]
    # return dp

n = 5
print(counting_bits(n))