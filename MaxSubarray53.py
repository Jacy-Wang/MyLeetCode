class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            curSum = 0
            maxSum = -2147483648
            for i in xrange(len(nums)):
                curSum = curSum + nums[i]
                maxSum = max(maxSum, curSum)
                curSum = max(0, curSum)
            return maxSum
