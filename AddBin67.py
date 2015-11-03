class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sign = False
        res = ""
        if len(b) > len(a):
            tmp = b
            b = a
            a = tmp
        diff = len(a) - len(b)
        for i in xrange(len(b) - 1, -1, -1):
            sign, tmp = Solution.getDigit(sign, a[i + diff], b[i])
            res = tmp + res
        for i in xrange(diff - 1, -1, -1):
            sign, tmp = Solution.getDigit(sign, a[i])
            res = tmp + res
        return '1' + res if sign else res

    @staticmethod
    def getDigit(sign, *args):
        if len(args) == 2:
            x = int(args[0])
            y = int(args[1])
            if sign:
                digit = (x ^ y) ^ 1
                sign = x | y == 1
            else:
                digit = x ^ y
                sign = x & y == 1
        elif len(args) == 1:
            x = int(args[0])
            digit = x
            if sign:
                digit = x ^ 1
                sign = x & 1 == 1
        return sign, str(digit)
