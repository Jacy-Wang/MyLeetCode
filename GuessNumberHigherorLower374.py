# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) / 2
            val = guess(mid)
            if val == 0:
                return mid
            elif val == -1:
                right = mid - 1
            else:
                left = mid + 1
