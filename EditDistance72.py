class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minDis = [[0 for _ in xrange(len(word1) + 1)] for _ in xrange(len(word2) + 1)]
        for j in xrange(1, len(word1) + 1):
            minDis[0][j] = j
        for i in xrange(1, len(word2) + 1):
            minDis[i][0] = i
            for j in xrange(1, len(word1) + 1):
                if word2[i - 1] == word1[j - 1]:
                    minDis[i][j] = minDis[i - 1][j - 1]
                else:
                    minDis[i][j] = minDis[i - 1][j - 1] + 1
                minDis[i][j] = min(minDis[i][j], minDis[i][j - 1] + 1, minDis[i - 1][j] + 1)
        return minDis[len(word2)][len(word1)]
