class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        length = len(prices)
        if length != 0:
            start = prices[0]
            for i in xrange(1, length):
                if prices[i] < prices[i - 1]:
                    profit += (prices[i - 1] - start)
                    start = prices[i]
                elif i == length - 1 and prices[i] >= prices[i - 1]:
                    profit += (prices[i] - start)
        return profit
