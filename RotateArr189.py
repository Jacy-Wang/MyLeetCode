class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        k = k % numsLen
        right = nums[numsLen - k :]
        left = nums[: numsLen - k]
        nums[:] = right + left
