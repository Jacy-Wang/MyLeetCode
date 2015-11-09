class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t == "":
            return True
        myDict = {}
        for i in xrange(len(s)):
            if s[i] not in myDict.keys():
                for v in myDict.keys():
                    if myDict[v] == t[i]:
                        return False
                myDict[s[i]] = t[i]
            else:
                if myDict[s[i]] != t[i]:
                    return False
        return True
