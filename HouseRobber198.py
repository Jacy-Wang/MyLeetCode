class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        if numsLen == 0:
            return 0
        elif numsLen == 1:
            return nums[0]
        val = [0 for _ in xrange(numsLen)]
        val[0] = nums[0]
        val[1] = max(nums[0], nums[1])
        for i in xrange(2, numsLen):
            val[i] = max(val[i - 1], val[i - 2] + nums[i])
        return val[numsLen - 1]
