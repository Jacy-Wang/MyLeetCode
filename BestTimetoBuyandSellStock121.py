class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MIN = 2147483647
        minPrice = MIN
        maxProfit = 0
        for i in xrange(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] > minPrice:
                curProfit = prices[i] - minPrice
                maxProfit = max(maxProfit, curProfit)
        return maxProfit
