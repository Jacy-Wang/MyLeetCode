class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [[1, 0] for _ in xrange(len(nums))]
        maxLen = 1
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[j] != nums[i] and dp[j][0] + 1 > dp[i][0]:
                    diff = nums[i] - nums[j]
                    if dp[j][1] == 0 or dp[j][1] * diff < 0:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = diff
            maxLen = max(maxLen, dp[i][0])
        return maxLen
