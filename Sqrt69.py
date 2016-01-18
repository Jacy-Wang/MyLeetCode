class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        start = 1
        end = x
        while start <= end:
            mid = start + (end - start) / 2
            if x / mid == mid:
                return mid
            elif x / mid < mid:
                end = mid - 1
            else:
                start = mid + 1
        return end
