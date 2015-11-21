class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        self.n = n
        self.k = k
        self.res = []
        self.do(0, [], 1)
        return self.res

    def do(self, curLen, curLst, idx):
        if curLen == self.k:
            self.res.append(curLst)
        else:
            for i in xrange(idx, self.n + 1):
                if not curLst or i > curLst[curLen - 1]:
                    curLst.append(i)
                    self.do(curLen + 1, curLst, idx + 1)
                    curLst = curLst[: curLen]
