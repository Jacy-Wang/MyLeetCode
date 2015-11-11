class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myDict = {}
        numsLen = len(nums)
        for i in xrange(numsLen):
            if nums[i] not in myDict.keys():
                myDict[nums[i]] = 1
            else:
                myDict[nums[i]] += 1
            if myDict[nums[i]] > numsLen / 2:
                return nums[i]
