class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        self.nums = nums
        self.res = []
        self.start = nums[0]
        self.myStr = str(self.start)
        for i in xrange(1, len(nums)):
            if nums[i] != self.start + 1:
                self.getStr(i)
                self.start = self.nums[i]
                self.myStr = str(self.start)
            else:
                self.start = nums[i]
        self.getStr(len(nums))
        return self.res
        
    def getStr(self, i):
        self.end = self.nums[i - 1]
        if int(self.myStr) == self.end:
            self.res.append(self.myStr)
        else:
            self.res.append(self.myStr + "->" + str(self.end))
