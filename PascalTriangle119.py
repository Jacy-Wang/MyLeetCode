class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        prev = [1]
        for i in xrange(1, rowIndex + 1):
            cur = []
            cur.append(1)
            for j in xrange(i - 1):
                cur.append(prev[j] + prev[j + 1])
            cur.append(1)
            prev = cur
        return prev
