class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        profit1 = [0 for _ in xrange(len(nums) - 1)]
        profit2 = [0 for _ in xrange(len(nums) - 1)]
        profit1[0] = nums[0]
        profit1[1] = max(nums[0], nums[1])
        for i in xrange(2, len(nums) - 1):
            profit1[i] = max(profit1[i - 1], profit1[i - 2] + nums[i])
        profit2[0] = nums[1]
        profit2[1] = max(nums[1], nums[2])
        for i in xrange(2, len(nums) - 1):
            profit2[i] = max(profit2[i - 1], profit2[i - 2] + nums[i + 1])
        return max(max(profit1), max(profit2))
