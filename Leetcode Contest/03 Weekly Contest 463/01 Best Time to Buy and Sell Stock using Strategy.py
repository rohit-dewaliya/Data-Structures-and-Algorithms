def max_profit(prices, strategy, k):
    # METHOD I---------------------------#
    # n = len(prices)
    #
    # base_profit = sum(strategy[i] * prices[i] for i in range(n))
    #
    # best_delta = 0
    #
    # for i in range(n - k + 1):
    #     original = 0
    #     new = 0
    #
    #     for j in range(k // 2):
    #         original += strategy[i + j] * prices[i + j]
    #
    #     for j in range(k // 2, k):
    #         original += strategy[i + j] * prices[i + j]
    #         new += prices[i + j]
    #
    #     delta = new - original
    #     best_delta = max(best_delta, delta)
    #
    # return base_profit + best_delta

    # METHOD II----------------------------#
    n = len(prices)

    base_profit = sum(strategy[i] * prices[i] for i in range(n))

    prefix_original = [0] * (n + 1)
    prefix_prices = [0] * (n + 1)

    for i in range(n):
        prefix_original[i + 1] = prefix_original[i] + strategy[i] * prices[i]
        prefix_prices[i + 1] = prefix_prices[i] + prices[i]

    best_delta = 0
    for L in range(n - k + 1):
        R = L + k
        mid = L + k // 2

        orig = prefix_original[R] - prefix_original[L]
        new = prefix_prices[R] - prefix_prices[mid]
        delta = new - orig

        best_delta = max(best_delta, delta)

    return base_profit + best_delta

prices = [4, 2, 8]
strategy = [-1, 0, 1]
k = 2
print(max_profit(prices, strategy, k))


'''
You are given two integer arrays prices and strategy, where:

prices[i] is the price of a given stock on the ith day.
strategy[i] represents a trading action on the ith day, where:
-1 indicates buying one unit of the stock.
0 indicates holding the stock.
1 indicates selling one unit of the stock.
You are also given an even integer k, and may perform at most one modification to strategy. A modification consists of:

Selecting exactly k consecutive elements in strategy.
Set the first k / 2 elements to 0 (hold).
Set the last k / 2 elements to 1 (sell).
The profit is defined as the sum of strategy[i] * prices[i] across all days.

Return the maximum possible profit you can achieve.

Note: There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.

Example 1:

Input: prices = [4,2,8], strategy = [-1,0,1], k = 2

Output: 10

Explanation:

Modification	Strategy	Profit Calculation	Profit
Original	[-1, 0, 1]	(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8	4
Modify [0, 1]	[0, 1, 1]	(0 × 4) + (1 × 2) + (1 × 8) = 0 + 2 + 8	10
Modify [1, 2]	[-1, 0, 1]	(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8	4
Thus, the maximum possible profit is 10, which is achieved by modifying the subarray [0, 1]​​​​​​​.

Example 2:

Input: prices = [5,4,3], strategy = [1,1,0], k = 2

Output: 9

Explanation:

Modification	Strategy	Profit Calculation	Profit
Original	[1, 1, 0]	(1 × 5) + (1 × 4) + (0 × 3) = 5 + 4 + 0	9
Modify [0, 1]	[0, 1, 0]	(0 × 5) + (1 × 4) + (0 × 3) = 0 + 4 + 0	4
Modify [1, 2]	[1, 0, 1]	(1 × 5) + (0 × 4) + (1 × 3) = 5 + 0 + 3	8
Thus, the maximum possible profit is 9, which is achieved without any modification.


Constraints ---------------#

2 <= prices.length == strategy.length <= 105
1 <= prices[i] <= 105
-1 <= strategy[i] <= 1
2 <= k <= prices.length
k is even
'''