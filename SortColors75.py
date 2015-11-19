class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        if numsLen > 0:
            self.nums = nums
            left = 0
            right = numsLen - 1
            i = 0
            while i <= right:
                if nums[i] == 0:
                    self.swap(i, left)
                    left = left + 1
                    i = i + 1
                elif nums[i] == 2:
                    self.swap(i, right)
                    right = right -1
                else:
                    i = i + 1
                    
    def swap(self, index1, index2):
        tmp = self.nums[index1]
        self.nums[index1] = self.nums[index2]
        self.nums[index2] = tmp
