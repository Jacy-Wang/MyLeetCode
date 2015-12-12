class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = sorted(candidates)
        self.target = target
        self.res = []
        self.search(0, 0, [])
        return self.res
        
    def search(self, pos, curSum, curLst):
        for i in xrange(pos, len(self.nums)):
            if curSum + self.nums[i] == self.target:
                self.res.append(curLst + [self.nums[i]])
            elif curSum + self.nums[i] < self.target:
                self.search(i, curSum + self.nums[i], curLst + [self.nums[i]])
