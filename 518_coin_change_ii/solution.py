class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        # Print the current Parameters
        print("Parameters - Coins: {coins}, Amount: {amount}".format(coins = coins, amount = amount))

        countup(coins, amount)

        return solutions

countup(coins, amount):
    for i in coins:
        for coin in coins:
            if i + coin == amount:
                print("solution found: ")
                return

    
