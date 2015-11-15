class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        tri = [[] for _ in xrange(numRows)]
        tri[0].append(1)
        for i in xrange(1, numRows):
            tri[i].append(1)
            for j in xrange(i - 1):
                tri[i].append(tri[i - 1][j] + tri[i - 1][j + 1])
            tri[i].append(1)
        return tri
