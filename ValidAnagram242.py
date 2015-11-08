class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t == "":
            return True
        if len(s) != len(t):
            return False
        myDict = {}
        for i in xrange(len(s)):
            if s[i] in myDict.keys():
                myDict[s[i]] += 1
            else:
                myDict[s[i]] = 1
        for i in xrange(len(t)):
            if t[i] not in myDict.keys():
                return False
            else:
                myDict[t[i]] -= 1
        return not any(myDict[v] != 0 for v in myDict.keys())
