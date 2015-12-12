import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rv = random.randint(0, len(nums) - 1)
        lst1 = []
        lst2 = []
        for val in nums:
            if val > nums[rv]:
                lst1.append(val)
            elif val < nums[rv]:
                lst2.append(val)
        if k <= len(lst1):
            return self.findKthLargest(lst1, k)
        if k > len(nums) - len(lst2):
            return self.findKthLargest(lst2, k - len(nums) + len(lst2))
        return nums[rv]
