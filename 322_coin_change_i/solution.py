class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # Base Case - if the target amount is 0, then it takes 0 coins to make up

        # Initialize minimum number of coins
        min_coins = 0

        # Iterate through each coin denomination
        for coin in coins:

            # If we decrease the amount to zero, then we're finished
            if amount - coin >= 0:
                # Recursively calculate the number of coins for the remaining amount
                num_coins = self.coinChange(coins, amount - coin)
                # If a valid solution is found, update the minimum number of coins
                if num_coins != -1:
                    min_coins = min(min_coins, num_coins + 1)

        # If no valid solution is found in the recursive loop
        if min_coins != 0:
            return min_coins
        else:
            return -1
