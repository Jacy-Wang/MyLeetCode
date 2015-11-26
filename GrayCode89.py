class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            prevCode = self.grayCode(n - 1)
            prevCodeLen = len(prevCode)
            const = 1 << (n - 1)
            right = [0 for _ in xrange(prevCodeLen)]
            for i in xrange(prevCodeLen - 1, -1, -1):
                right[prevCodeLen - i - 1] = prevCode[i] + const
            return prevCode + right
