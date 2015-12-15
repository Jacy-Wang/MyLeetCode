class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        self.mapping = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.digits = digits
        self.res = []
        self.get("")
        return self.res
        
    def get(self, curStr):
        if len(curStr) == len(self.digits):
            self.res.append(curStr)
        else:
            s = self.mapping[int(self.digits[len(curStr)])]
            for i in xrange(len(s)):
                self.get(curStr + s[i])
