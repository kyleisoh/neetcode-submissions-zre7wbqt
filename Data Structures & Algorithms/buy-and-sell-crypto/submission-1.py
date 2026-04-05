class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(prices[j] - prices[i], max_profit)
        
        return max_profit

    
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]

        return max_profit
