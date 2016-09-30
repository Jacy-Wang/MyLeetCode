class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for _ in xrange(target + 1)]
        dp[0] = 1
        for i in xrange(1, target + 1):
            for j in nums:
                if j <= i:
                    dp[i] += dp[i - j]
        return dp[target]
