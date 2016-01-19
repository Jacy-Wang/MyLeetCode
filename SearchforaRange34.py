class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        self.nums = nums
        self.target = target
        left = self.find(True)
        right = self.find(False)
        return [left, right]

    def find(self, sign):
        start = 0
        end = len(self.nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if self.nums[mid] == self.target:
                if sign:
                    end = mid - 1
                else:
                    start = mid + 1
            elif self.nums[mid] < self.target:
                start = mid + 1
            else:
                end = mid - 1
        if sign:
            if 0 <= start < len(self.nums) and self.nums[start] == self.target:
                return start
            return -1
        else:
            if 0 <= end < len(self.nums) and self.nums[end] == self.target:
                return end
            return -1           
