def climb_stairs(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n <= 2:
        return n

    memo[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
    return memo[n]

# def climb_stairs(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     return climb_stairs(n - 1) + climb_stairs(n - 2)

n = 10
print(climb_stairs(n))