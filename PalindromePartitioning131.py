import copy
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        length = len(s)
        if length == 0:
            return [[]]
        self.s = s
        self.length = length
        self.tellPalindrome()
        self.res = []
        self.getPartitions(0, [])
        return self.res

    def tellPalindrome(self):
        self.isPalindrome = [[False for _ in xrange(self.length)] for _ in xrange(self.length)]
        self.isPalindrome[0][0] = True
        for i in xrange(1, self.length):
            self.isPalindrome[i][i] = True
            self.isPalindrome[i - 1][i] = (self.s[i] == self.s[i - 1])
        for i in xrange(2, self.length):
            for j in xrange(i - 1):
                self.isPalindrome[j][i] = (self.s[i] == self.s[j]) and self.isPalindrome[j + 1][i - 1]

    def getPartitions(self, start, lst):
        if start == self.length:
            self.res.append(copy.deepcopy(lst))
        else:
            for i in xrange(start, self.length):
                if self.isPalindrome[start][i]:
                    lst.append(self.s[start : i + 1])
                    self.getPartitions(i + 1, lst)
                    lst[:] = lst[: len(lst) - 1]
