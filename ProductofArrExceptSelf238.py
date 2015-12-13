class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for _ in xrange(len(nums))]
        mul = 1
        for i in xrange(len(nums)):
            res[i] *= mul
            mul *= nums[i]
        mul = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] *= mul
            mul *= nums[i]
        return res
