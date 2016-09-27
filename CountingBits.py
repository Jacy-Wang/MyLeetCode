class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        res = [0, 1]
        n = 1
        while 2 ** (n + 1) <= num:
            res.extend([v + 1 for v in res])
            n += 1
        res.extend([res[i] + 1 for i in xrange(num - 2 ** n + 1)])
        return res
