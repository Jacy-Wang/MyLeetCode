class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        return self.compute(num, target, '', 1)

    def leadingZeroes(self, string):
        return string.startswith("00") or int(string) and string.startswith("0")

    def compute(self, string, target, mulExpr = '', mulVal = 1):
        ans = []
        if not string:
            return ans
        if self.leadingZeroes(string):
            pass
        elif int(string) * mulVal == target:
            ans.append(string + mulExpr)
        for i in xrange(len(string) - 1):
            left = string[: i + 1]
            right = string[i + 1 :]
            if not self.leadingZeroes(right):
                rightExpr = right + mulExpr
                rightVal = int(right) * mulVal
                for v in self.compute(left, target - rightVal):
                    ans.append(v + "+" + rightExpr)
                for v in self.compute(left, target + rightVal):
                    ans.append(v + "-" + rightExpr)
                for v in self.compute(left, target, "*" + rightExpr, rightVal):
                    ans.append(v)
        return ans
