class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        coins.sort()
        pointer = n - 1
        count = 0
        while pointer >= 0 and amount >= 0:
            print(pointer, coins[pointer], amount, count)
            if amount - coins[pointer] < 0:
                pointer -= 1
            else:
                amount -= coins[pointer]
                count += 1
        if amount == 0:
            return count
        else:
            return -1


coins = [186, 419, 83, 408]
amount = 6249
print(Solution().coinChange(coins, amount))