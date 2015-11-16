class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [nums]
        self.nums = nums
        self.numsLen = len(nums)
        sign = [0 for _ in xrange(self.numsLen)]
        self.res = []
        self.do(sign, 0, [])
        return self.res
        
    def do(self, sign, curLen, curRes):
        if curLen == self.numsLen:
            self.res.append(curRes)
        else:
            for i in xrange(self.numsLen):
                if not sign[i]:
                    sign[i] = 1
                    curRes.append(self.nums[i])
                    self.do(sign, curLen + 1, curRes)
                    sign[i] = 0
                    curRes = curRes[: curLen]
