class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0 for _ in xrange(n + 1)]
        nums[0] = 1
        nums[1] = 1
        for i in xrange(2, n + 1):
            for j in xrange(i):
                nums[i] += nums[j] * nums[i - j - 1]
        return nums[n]
