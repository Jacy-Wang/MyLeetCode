class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        self.title = ""
        self. getTitle(n)
        return self.title
            
    def getTitle(self, n):
        first = n / 26
        second = n % 26
        if second == 0:
            self.title = "Z" + self.title
            first = first - 1
        else:
            self.title = chr(64 + second) + self.title
        if 1 <= first <= 26:
            self.title = chr(64 + first) + self.title
        elif first > 26:
            self.getTitle(first)
