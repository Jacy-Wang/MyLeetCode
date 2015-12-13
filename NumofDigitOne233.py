ass Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 1
        num = 0
        while base <= n:
            left = n / base
            right = n % base
            digit = left % 10
            mul = left / 10
            if digit == 0:
                num += mul * base
            elif digit == 1:
                num += mul * base + right + 1
            else:
                num += (mul + 1) * base
            base *= 10
        return num
