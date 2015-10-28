class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        minLength = len(strs[0])
        minStr = strs[0]
        for v in strs:
            if len(v) < minLength:
                minLength = len(v)
                minStr = v
        for i in xrange(minLength):
            for v in strs:
                if v[i] != minStr[i]:
                    return minStr[: i] if i != 0 else ''
        return minStr
