class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos1 = pos2 = 0
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i - 1] and not pos1:
                pos1 = i
                curVal = nums[pos1]
            if pos1:
                sign = False
                for j in xrange(pos2 + 1, len(nums)):
                    if nums[j] > curVal:
                        pos2 = j
                        curVal = nums[pos2]
                        nums[pos1] = nums[pos2]
                        pos1 = pos1 + 1
                        sign = True
                        break
                if not sign:
                    return pos1
        return len(nums)
