class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left and right pointer
        
        maxP = 0
        # iterate through prices
        while r < len(prices):
            # if profitable transaction calculate potential profit
            if prices[l] < prices[r]:
                maxP = max(prices[r] - prices[l], maxP)
            # otherwise move left to new low point
            else:
                l = r
            r += 1
        return maxP
                