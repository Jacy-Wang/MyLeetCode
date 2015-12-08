class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return -1
        self.s = s
        self.length = length
        self.tellPalindrome()
        minCuts = [length for _ in xrange (length + 1)]
        minCuts[0] = -1
        for i in xrange(1, length + 1):
            for j in xrange(i):
                if self.isPalindrome[j][i - 1]:
                    minCuts[i] = min(minCuts[i], minCuts[j] + 1)
        return minCuts[length]
      
    def tellPalindrome(self):
        self.isPalindrome = [[False for _ in xrange(self.length)] for _ in xrange(self.length)]
        self.isPalindrome[0][0] = True
        for i in xrange(1, self.length):
            self.isPalindrome[i][i] = True
            self.isPalindrome[i - 1][i] = (self.s[i - 1] == self.s[i])
        for i in xrange(2, self.length):
            for j in xrange(i - 1):
                self.isPalindrome[j][i] = (self.s[j] == self.s[i]) and self.isPalindrome[j + 1][i - 1]
