class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = 0
        numsLength = len(nums)
        for i in xrange(numsLength):
            if nums[i] == 0:
                counter = counter + 1
            else:
                nums[i - counter] = nums[i]
        nums[numsLength - counter :] = [0] * counter
