import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n = n / 4
        if n % 8 == 7:
            return 4
        i = 0
        while i ** 2 < n:
            num = int(math.sqrt(n - i ** 2))
            if num ** 2 + i ** 2 == n:
                return 1 if i == 0 else 2
            i += 1
        return 3
