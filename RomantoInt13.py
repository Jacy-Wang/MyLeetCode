class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        keyVal = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        num = 0
        if len(s) != 0:
            for i in xrange(1, len(s)):
                previous = s[i - 1]
                current = s[i]
                if keyVal[previous] >= keyVal[current]:
                    num = num + keyVal[previous]
                else:
                    num = num - keyVal[previous]
            num = num + keyVal[s[len(s) - 1]]
        return num
