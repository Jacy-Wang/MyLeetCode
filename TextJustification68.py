class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth == 0:
            return [""]
        self.words = words
        self.maxWidth = maxWidth
        self.res = []
        curWidth = len(words[0])
        startIndex = 0
        for i in xrange(1, len(words)):
            curWidth += (len(words[i]) + 1)
            if curWidth > maxWidth:
                self.makeLine(startIndex, i - 1, curWidth - len(words[i]) - 1, False)
                startIndex = i
                curWidth = len(words[i])
        self.makeLine(startIndex, len(words) - 1, curWidth, True)
        return self.res
        
    def makeLine(self, start, end, width, sign):
        line = ""
        if sign or start == end:
            for i in xrange(start, end):
                line += self.words[i]
                line += " "
            line += self.words[end]
            line += " " * (self.maxWidth - len(line))
        else:
            num = (self.maxWidth - width) / (end - start)
            residual = (self.maxWidth - width) % (end - start)
            for i in xrange(start, end):
                line += self.words[i]
                line += " " * (num + 1)
                if i - start + 1 <= residual:
                    line += " "
            line += self.words[end]
        self.res.append(line)
