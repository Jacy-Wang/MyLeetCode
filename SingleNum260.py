class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xorVal = nums[0]
        for i in xrange(1, len(nums)):
            xorVal ^= nums[i]
        lowestOne = xorVal & -xorVal
        e1, e2 = 0, 0
        for v in nums:
            if v & lowestOne:
                e1 ^= v
            else:
                e2 ^= v
        return [e1, e2]
