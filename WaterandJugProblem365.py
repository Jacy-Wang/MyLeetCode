class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False
        if z == 0:
            return True
        val = self.gcd(min(x, y), max(x, y))
        if val == 1:
            return True
        return z % val == 0
        
    def gcd(self, m, n):
        if m == 0:
            return n
        elif m == n:
            return n
        return self.gcd(n % m, m)
