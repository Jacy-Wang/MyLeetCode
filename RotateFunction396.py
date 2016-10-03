class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        prevDiff = 0
        s = sum(A)
        for i in xrange(len(A) - 1):
            diff = s - len(A) * A[len(A) - 1 - i]
            res = max(res, diff + prevDiff)
            prevDiff += diff
        return res + sum([i * A[i] for i in xrange(len(A))]) if A else 0
