class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end and nums[start] >= nums[end]:
            mid = (start + end) / 2
            if nums[mid] > nums[start]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                start += 1
        return nums[start]
