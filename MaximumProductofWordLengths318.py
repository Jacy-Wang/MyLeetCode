class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxLen = 0
        num = [0 for _ in xrange(len(words))]
        for i in xrange(len(words)):
            num[i] = sum([1 << (ord(v) - ord('a')) for v in set(words[i])])
        for i in xrange(len(num) - 1):
            for j in xrange(i + 1, len(num)):
                if num[i] & num[j] == 0:
                    maxLen = max(maxLen, len(words[i]) * len(words[j]))
        return maxLen
