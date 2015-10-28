class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        keyVal = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
        res = ""
        for i in xrange(3, -1, -1):
            d = num / 10 ** i
            num = num % 10 ** i
            if 1 <= d <= 3:
                res = res + keyVal[10 ** i] * d
            elif d == 4:
                res = res + keyVal[10 ** i] + keyVal[5 * 10 ** i]
            elif 5 <= d <= 8:
                res = res + keyVal[5 * 10 ** i] + keyVal[10 ** i] * (d - 5)
            elif d == 9:
                res = res + keyVal[10 ** i] + keyVal[10 ** (i + 1)]
        return res
