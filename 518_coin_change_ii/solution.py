class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        # Add zero for Dynamic Programming Table (DPT) index
        coins = [0] + coins

        # Print the current Parameters
        print("Parameters - Coins: {coins}, Amount: {amount}".format(coins = coins, amount = amount))

        # Fill the DPT
        dp = []

        # The y-axis of the DPT is the index of each coin in the coin list
        for y in range(len(coins)):             

            # Set DPT Row 
            dpr = [0] * (amount + 1)

            # The x-axis of the DPT is every number counting to the amount needed
            for x in range(amount + 1):
                print("x: {xv}, y: {yv}, coin: {cv}".format(xv = x, yv = y, cv = coins[y]))

                # Zero Case
                if y == 0:
                    if x == 0:
                        dpr[x] = 1
                    else:
                        dpr[x] = 0

                # Logic Case
                else:
                    # If we exclude the coin from the total, use the previous coins result and copy over
                    exclude = dp[y-1][x]
                    print("Excluded: " + str(exclude))

                    # If we include the coin, subtract the coins value from the total
                    include = x - coins[y]
                    print("Include:  " + str(include))

                    if include < 0:
                        # If the include is below zero, just use the exclude value
                        value = exclude
                    else:
                        # Otherwise, add the exclude value to the index of the remainder in the DPT
                        value = dpr[include] + exclude
                    
                    print("Value:    " + str(value))

                    # Write the calculated value to the DPT at the current index
                    dpr[x] = value

            # When each row has been calculated add it to the DPT
            dp.append(dpr)

        for array in dp:
            print(array)

        # The last item in the DPT is the answer
        return(dp[-1][-1])
