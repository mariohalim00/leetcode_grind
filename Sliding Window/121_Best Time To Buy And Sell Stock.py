class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        str_len = len(prices)
        max_profit = 0
        while(i <= (str_len - 1) and j <= ( str_len - 1)):
            diff = prices[j] - prices[i]
            if(diff < 0):
                i = j
                j = i + 1
            else:
                max_profit = max(max_profit, diff)
                j += 1
        return max_profit
