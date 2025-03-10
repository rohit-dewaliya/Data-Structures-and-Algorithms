def maxProfitRecursive(prices):
    n = len(prices)
    no_stock = 0
    has_stock = -prices[0]

    for i in range(1, n):
        no_stock = max(no_stock, has_stock + prices[i])
        has_stock = max(has_stock, no_stock - prices[i])

    return no_stock

    '''
    Solution I---------------------------------#
    def dfs(i, holding):
        if i == len(prices):
            return 0

        max_profit = dfs(i + 1, holding)

        if holding:
            max_profit = max(max_profit, prices[i] + dfs(i + 1, False))
        else:
            max_profit = max(max_profit, -prices[i] + dfs(i + 1, True))

        return max_profit

    return dfs(0, False)

    Solution II----------------------------------#
    profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    '''

# Example usage
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfitRecursive(prices))  # Output: 7
