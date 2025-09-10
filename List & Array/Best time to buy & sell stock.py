'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

# Brute Force approach --
'''
def maxProfit(prices):
    # Initialize max_profit to 0 (if no profit possible, result stays 0)
    max_profit = 0

    # Outer loop → choose a buying day i
    for i in range(len(prices)):
        # Inner loop → choose a selling day j (must be after i)
        for j in range(i + 1, len(prices)):
            # Calculate profit if we buy on day i and sell on day j
            profit = prices[j] - prices[i]

            # Update max_profit if this profit is greater
            if profit > max_profit:
                max_profit = profit

    # After checking all pairs, return the best profit found
    return max_profit
'''

# Optimal solution --

def maxProfit(prices):

    # If the list is empty, no transaction can be made → return 0
    if not prices:
        return 0

    # Initialize variables
    # min_price → keeps track of the lowest price seen so far (best buying price)
    # max_profit → keeps track of the best profit achievable so far
    min_price = float('inf')
    max_profit = 0

    # Loop through each day's stock price
    for p in prices:
        # Check if selling today (p) after buying at min_price gives better profit
        if p - min_price > max_profit:
            max_profit = p - min_price

        # Update min_price if today's price is smaller (better to buy here)
        if p < min_price:
            min_price = p

    # Return the maximum profit found after scanning all prices
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
