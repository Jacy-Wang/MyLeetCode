class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 2:
            if num % 2 == 0:
                num = num / 2
                return self.isUgly(num)
            elif num % 3 == 0:
                num = num / 3
                return self.isUgly(num)
            elif num % 5 == 0:
                num = num / 5
                return self.isUgly(num)
            else:
                return False
        return num == 1
