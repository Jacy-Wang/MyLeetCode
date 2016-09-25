class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return 0 if amount == 0 else -1
        MAX = 2147483647
        dp = [MAX for _ in xrange(amount + 1)]
        dp[0] = 0
        for i in xrange(amount + 1):
            if dp[i] < MAX:
                for v in coins:
                    if i + v <= amount:
                        dp[i + v] = min(dp[i + v], dp[i] + 1)
        return dp[amount] if dp[amount] < MAX else -1
