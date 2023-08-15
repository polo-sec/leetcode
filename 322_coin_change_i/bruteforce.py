class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # Base case: if the target amount is 0, it takes 0 coins to make up
        # This both sets our first minimum value, and also gives us a 
        if amount == 0:
            return 0
        
        # Initialize minimum number of coins to a value larger than any possible result
        # When we iterate through each coin denomination, min_coins is updated if smaller
        # Setting it to +int max, garuntees the first result found is smaller.
        min_coins = float('inf')
        
        # Iterate through each coin denomination
        for coin in coins:
            if amount - coin >= 0:
                print(f"Trying coin {coin} for amount {amount}")
                
                # Recursively calculate the number of coins for the remaining amount
                num_coins = self.coinChange(coins, amount - coin)
                print(f"Number of coins for amount {amount - coin}: {num_coins}")
                
                # If a valid solution is found, update the minimum number of coins
                # Use the smallest value out of the current minimum coins, and the new number of coins
                if num_coins != -1:
                    min_coins = min(min_coins, num_coins + 1)
        
        # If no valid solution is found, set min_coins to -1
        min_coins = min_coins if min_coins != float('inf') else -1
        return min_coins

