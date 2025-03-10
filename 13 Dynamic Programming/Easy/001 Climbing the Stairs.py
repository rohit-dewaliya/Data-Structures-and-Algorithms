def climb_stairs(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n <= 2:
        return n

    memo[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
    return memo[n]

n = 40
print(climb_stairs(n))