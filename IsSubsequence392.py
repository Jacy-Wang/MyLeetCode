class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ps = 0
        pt = 0
        while ps < len(s) and pt < len(t):
            if t[pt] == s[ps]:
                ps += 1
            pt += 1
        return ps == len(s)
