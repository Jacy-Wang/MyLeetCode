class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = sorted(candidates)
        self.target = target
        self.res = []
        self.search(-1, 0, [])
        return self.res
        
    def search(self, prevPos, curSum, curLst):
        for i in xrange(prevPos + 1, len(self.nums)):
            if curSum + self.nums[i] == self.target:
                if curLst + [self.nums[i]] not in self.res:
                    self.res.append(curLst + [self.nums[i]])
            elif curSum + self.nums[i] < self.target:
                self.search(i, curSum + self.nums[i], curLst + [self.nums[i]])
