class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MAXINT = 2147483647
        sign = False
        nums = sorted(nums)
        diff = MAXINT
        for i in xrange(len(nums) - 2):
            curTarget = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curDiff = curTarget - nums[left] - nums[right]
                if abs(curDiff) < abs(diff):
                    diff = curDiff
                if curDiff == 0:
                    sign = True
                    break
                elif curDiff < 0:
                    right -= 1
                else:
                    left += 1
            if sign:
                return target
        return target - diff
