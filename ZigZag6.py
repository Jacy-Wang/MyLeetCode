class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        sLength = len(s)
        r = ''
        if numRows == 1:
            return s
        elif numRows == 2:
            numCols = (sLength + 1) / 2
            for i in xrange(numCols):
                r = r + s[2 * i]
            for i in xrange(numCols, sLength):
                r = r + s[2 * (i - numCols) + 1]
            return r
        else:
            numCols = sLength / (numRows - 1)
            if 0 < sLength % (numRows - 1) <= numRows:
                numCols = numCols + 1
            elif sLength % (numRows - 1) > numRows:
                numCols = numCols + 2
            for i in xrange(numRows):
                for j in xrange(numCols):
                    if j % 2 == 0:
                        curIndex = (j / 2) * (2 * numRows - 2) + i
                        if curIndex < sLength:
                            r = r + s[curIndex]
                    elif 0 < i < numRows - 1:
                        curIndex = ((j + 1) / 2) * numRows + ((j - 1) / 2) * (numRows - 2) + numRows - 2 - i
                        if curIndex < sLength:
                            r = r + s[curIndex]
            return r
