class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        match = [[False for _ in xrange(len(s2) + 1)] for _ in xrange(len(s1) + 1)]
        match[0][0] = True
        for i in xrange(len(s1)):
            if s1[i] == s3[i]:
                match[i + 1][0] = match[i][0]
        for j in xrange(len(s2)):
            if s2[j] == s3[j]:
                match[0][j + 1] = match[0][j]
        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                match[i + 1][j + 1] = (s3[i + j + 1] == s1[i] and match[i][j + 1]) or (s3[i + j + 1] == s2[j] and match[i + 1][j])
        return match[len(s1)][len(s2)]
