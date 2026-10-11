# ou are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

class Solution:
    # brute-force shreyash
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            current_profit = 0
            for j in range(i+ 1 , len(prices)):
                if(prices[j] > prices[i] ):
                    current_profit = prices[j] - prices[i]
                    max_profit = max(max_profit , current_profit)

        return max_profit

    # optimize Shreyash 
    def maxProfitOptimize(self, prices: list[int]) -> int:
            max_profit = 0
            n = len(prices)
            i = 0
            j = 1
            while(j < n  ):
                if(prices[i] >= prices[j]):
                    i = j 
                    j += 1
                else:
                    max_profit = max(max_profit , prices[j]- prices[i])
                    j += 1    
                

            return max_profit

    def maxProfitChtGpt(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)

            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
                 
                 
            

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]

s1 = Solution()
print(s1.maxProfit(prices))
print(s1.maxProfitOptimize(prices))


