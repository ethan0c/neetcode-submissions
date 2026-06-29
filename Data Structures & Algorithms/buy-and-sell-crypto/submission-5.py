class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = prices[0], 0
        profit = sell

        for i in range (1,len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
        