class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0 for _ in xrange(n + 1)]
        for i in xrange(1, n + 1):
            if i == 1:
                nums[1] = 1
            elif i == 2:
                nums[2] = 2
            else:
                nums[i] = nums[i - 1] + nums[i - 2]
        return nums[n]
