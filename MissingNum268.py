class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        maxNum = max(nums)
        if maxNum == length:
            return sum(range(length + 1)) - sum(nums)
        else:
            return length
