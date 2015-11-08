# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        return self.find(1, n)
        
    def find(self, start, end):
        if end == start + 1:
            return end
        else:
            mid = (start + end) / 2
            if isBadVersion(mid):
                return self.find(start, mid)
            else:
                return self.find(mid, end)
