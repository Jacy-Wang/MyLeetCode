class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left = 2
        right = int(math.ceil(num / 2.0))
        while left <= right:
            mid = (left + right) / 2
            val = mid ** 2
            if val == num:
                return True
            elif val < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
