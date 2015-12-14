class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            counter = 0
            for v in nums:
                if v <= mid:
                    counter += 1
            if counter > mid:
                end = mid - 1
            else:
                start = mid + 1
        return start
