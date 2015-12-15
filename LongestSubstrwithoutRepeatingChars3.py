class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = {}
        maxLen = 0
        i = 0
        while i < len(s):
            if s[i] not in myDict:
                myDict[s[i]] = i
                i += 1
            else:
                maxLen = max(maxLen, len(myDict))
                i = myDict[s[i]] + 1
                myDict = {}
        return max(maxLen, len(myDict))
