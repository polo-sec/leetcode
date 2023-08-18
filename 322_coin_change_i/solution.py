class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        coins = [0] + coins

        print(coins)

        dpt = []

        # Iterate over the y axis of the table, each coin to be used
        for y in range(len(coins)):

            dpr = [0] * (amount + 1)

            print(f"Coin: {coins[y]}")

            # Iterate overthe x axis of the table, the amount to solve
            for x in range(amount+1):
                print(f"Amount: {x}")

                # Zero Case
                if coins[y] == 0:
                    if x == 0:
                        dpr[x] = 1
                    else:
                        dpr[x] = 0

                # Logic Case
                else:

                    # Exclude Curent Coin
                    print(f"Exclude: {dpt[y-1][x]}")
                    exclude = dpt[y-1][x]

                    # Include Current Coin
                    if x - coins[y] < 0:
                        print(f"Invalid Calc: {x} - {coins[y]} = {x - coins[y]}")
                        dpr[x] = exclude
                    else:
                        subtraction = x - coins[y]
                        print(f"Valid Calc: {x} - {coins[y]} = {subtraction}")
                        dpr[x] = dpr[subtraction] + exclude


            dpt.append(dpr)

        for row in dpt:
            print(row)

        return min_coins

