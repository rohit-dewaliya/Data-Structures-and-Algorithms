# Using Memoization from Dynamic Programming
def fib(n, memo = {}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n <= 2:
        return 1
    result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return memo[n]

# Using Tabulization from Dynamic Programming
def find_fib(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

n = 50
print(fib(n))