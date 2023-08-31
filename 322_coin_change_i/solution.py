class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # As we're dealing with a recursive problem, we can speed it up using memoization
        # we implement this with a calculation cache.
        coin_memo = {}

        # We have to nest another function in the class, to make coin_memo common across
        # recursive loops
        def coinChangeHelper(target_amount):

            # Check if the solution has already been memoized
            if target_amount in coin_memo:
                print(f"Found amount {target_amount} in memo {coin_memo}")
                return coin_memo[target_amount]

            # Base case: if the target amount is 0, it takes 0 coins to make up
            # This both sets our first minimum value, and also gives us a 
            if target_amount == 0:
                return 0
            
            # Initialize minimum number of coins to a value larger than any possible result
            # When we iterate through each coin denomination, min_coins is updated if smaller
            # Setting it to +int max, garuntees the first result found is smaller.
            min_coins = float('inf')

            
            # Iterate through each coin denomination
            for coin in coins:
                if target_amount - coin >= 0:
                    print(f"Trying coin {coin} for target_amount {amount}")
                    
                    # Recursively calculate the number of coins for the remaining target_amount
                    num_coins = coinChangeHelper(target_amount - coin)
                    print(f"Number of coins for target_amount {amount - coin}: {num_coins}")
                    
                    # If a valid solution is found, update the minimum number of coins
                    # Use the smallest value out of the current minimum coins, and the new number of coins
                    if num_coins != -1:
                        min_coins = min(min_coins, num_coins + 1)
            
            # If no valid solution is found, set min_coins to -1
            if min_coins == float('inf'):
                coin_memo[target_amount] = -1
            else:
                coin_memo[target_amount] = min_coins

            return coin_memo[target_amount]

        return coinChangeHelper(amount)



