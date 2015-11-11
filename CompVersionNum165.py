class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        len1 = len(v1)
        len2 = len(v2)
        for i in xrange(max(len1, len2)):
            val1 = 0
            val2 = 0
            if i < len1:
                val1 = int(v1[i])
            if i < len2:
                val2 = int(v2[i])
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
        return 0
