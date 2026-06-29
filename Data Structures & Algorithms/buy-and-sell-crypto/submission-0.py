class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = prices[0], 0
        profit = 0

        length = len(prices)
        for i in range (1,length):
            if buy > prices[i]:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
        