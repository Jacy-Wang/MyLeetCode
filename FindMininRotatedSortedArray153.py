class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        self.nums = nums
        return self.binarySearch(0, length - 1)
            
    def binarySearch(self, start, end):
        if start == end:
            return self.nums[start]
        elif start == end - 1:
            return min(self.nums[start], self.nums[end])
        else:
            if self.nums[start] < self.nums[end]:
                return self.nums[start]
            else:
                mid = (start + end) / 2
                if self.nums[mid] > self.nums[end]:
                    return self.binarySearch(mid, end)
                else:
                    return self.binarySearch(start, mid)
