class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.k = k
        self.res = []
        self.search(0, 0, [])
        return self.res

    def search(self, pos, curSum, curLst):
        if len(curLst) == self.k:
            if curSum == self.n:
                self.res.append(curLst)
        else:
            for i in xrange(pos + 1, 10):
                if curSum + i <= self.n:
                    self.search(i, curSum + i, curLst + [i])
