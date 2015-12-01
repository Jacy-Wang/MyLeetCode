class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        left = [0 for _ in xrange(length)]
        right = [0 for _ in xrange(length)]
        minPrice = prices[0]
        for i in xrange(1, length):
            left[i] = max(left[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        maxPrice = prices[length - 1]
        for i in xrange(length - 3, -1, -1):
            right[i] = max(right[i + 1], maxPrice - prices[i + 1])
            maxPrice = max(maxPrice, prices[i + 1])
        maxProfit = 0
        for i in xrange(length):
            maxProfit = max(left[i] + right[i], maxProfit)
        return maxProfit
