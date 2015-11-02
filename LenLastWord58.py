class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip(" ")
        if len(s) == 0:
            return 0
        arr = s.split(" ")
        return len(arr[len(arr) - 1])
