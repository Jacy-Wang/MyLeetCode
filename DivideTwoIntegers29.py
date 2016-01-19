class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        if dividend == 0:
            return 0
        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            return 0 - dividend
        if divisor == 1:
            return dividend
        d = abs(dividend)
        r = abs(divisor)
        res = 0
        while d >= r:
            cusum = r
            count = 1
            while cusum + cusum <= d:
                cusum += cusum
                count += count
            res += count
            d -= cusum
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res
