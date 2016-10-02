class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            if c not in d.keys():
                return c
            else:
                d[c] = d.get(c) - 1
                if d[c] == -1:
                    return c
