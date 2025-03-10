'''
def buy_sell_stocks(prices):
    n = len(prices)
    min_price = float('inf')
    max_profit = 0
    for i in range(0, n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)

    return max_profit
'''

def buy_sell_stocks(prices):
    n = len(prices)
    if not prices or n < 2:
        return 0
    max_profit = 0
    left_buy = 0
    right_sell = 1

    while right_sell < n:
        current_price = prices[right_sell]
        buy_price = prices[left_buy]
        if buy_price < current_price:
            current_profit = current_price - buy_price
            max_profit = max(max_profit, current_profit)
        else:
            left_buy = right_sell
        right_sell += 1
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(buy_sell_stocks(prices))