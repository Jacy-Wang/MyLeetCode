class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        seqDict = {}
        res = []
        for i in xrange(length - 9):
            seqDict[s[i : i + 10]] = seqDict.get(s[i : i + 10], 0) + 1
        for k, v in seqDict.items():
            if v >= 2:
                res.append(k)
        return res
