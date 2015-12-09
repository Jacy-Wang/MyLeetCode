class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return self.find(0, len(nums) - 1)

    def find(self, start, end):
        if start == end:
            return start
        elif start + 1 == end:
            if self.nums[start] > self.nums[end]:
                return start
            else:
                return end
        else:
            mid = (start + end) / 2
            if self.nums[mid] < self.nums[mid - 1]:
                return self.find(start, mid)
            else:
                return self.find(mid, end)
