class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        myDict = {}
        prev = n
        while 1:
            cur = 0
            s = str(prev)
            for i in xrange(len(s)):
                cur = cur + int(s[i]) ** 2
            if cur == 1:
                return True
            elif cur in myDict.keys():
                return False
            else:
                myDict[cur] = 1
            prev = cur
