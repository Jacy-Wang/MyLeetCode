class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.res = []
        self.recursiveGen(0, 0, "")
        return self.res
        
    def recursiveGen(self, leftNum, rightNum, s):
        if leftNum == rightNum == self.n:
            self.res.append(s)
            return
        if leftNum < self.n:
            self.recursiveGen(leftNum + 1, rightNum, s + "(")
        if rightNum < leftNum <= self.n:
            self.recursiveGen(leftNum, rightNum + 1, s + ")")
        return
