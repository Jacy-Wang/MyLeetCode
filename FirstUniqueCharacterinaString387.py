class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c, i in zip(s, xrange(len(s))):
            old = d.get(c, [0, None])
            d[c] = [old[0] + 1, i]
        idx = -1
        for val in d.values():
            if val[0] == 1:
                if idx == -1 or val[1] < idx:
                    idx = val[1]
        return idx
