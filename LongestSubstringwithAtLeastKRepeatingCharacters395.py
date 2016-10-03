class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        self.k = k
        self.cand = []
        self.find(s)
        return max([len(v) for v in self.cand]) if self.cand else 0

    def find(self, s):
        if s:
            d = {}
            for v in s:
                d[v] = d.get(v, 0) + 1
            charSet = {}
            for key, val in d.items():
                if val < self.k:
                    charSet[key] = 1
            if not charSet:
                self.cand.append(s)
            else:
                start = 0
                for i in xrange(len(s)):
                    if s[i] in charSet.keys():
                        if i - start >= self.k:
                            self.find(s[start : i])
                        start = i + 1
                if len(s) - start >= self.k:
                    self.find(s[start :])
