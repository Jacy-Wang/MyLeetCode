class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = len(nums) - 1
        for i in xrange(len(nums)):
            sign = False
            if pos < i:
                return i
            elif pos == i:
                return i + 1 if nums[i] != val else i
            if nums[i] == val:
                for j in xrange(pos, i, -1):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        pos = j - 1
                        sign = True
                        break
                if not sign:
                    return i
