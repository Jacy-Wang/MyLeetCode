# buy[i]  = max(rest[i-1]-price, buy[i-1]) 
# sell[i] = max(buy[i-1]+price, sell[i-1])
# rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
# One tricky point is how do you make sure you sell before you buy, since from the equations it seems that [buy, rest, buy] is entirely possible.

# Well, the answer lies within the fact that buy[i] <= rest[i] which means rest[i] = max(sell[i-1], rest[i-1]). That made sure [buy, rest, buy] is never occurred.

# A further observation is that and rest[i] <= sell[i] is also true therefore

# rest[i] = sell[i-1]
# Substitute this in to buy[i] we now have 2 functions instead of 3:

# buy[i] = max(sell[i-2]-price, buy[i-1])
# sell[i] = max(buy[i-1]+price, sell[i-1])

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = -prices[0]
        prevBuy = 0
        sell = 0
        prevSell = 0
        for i in xrange(1, len(prices)):
            prevBuy = buy
            buy = max(prevSell - prices[i], prevBuy)
            prevSell = sell
            sell = max(prevBuy + prices[i], prevSell)
        return sell
