class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        myStr = (filter(str.isalnum, str(s))).lower()
        print myStr
        if len(s) == 1:
            return True
        strLen = len(myStr)
        i = 0
        j = strLen - 1
        while j >= (strLen + 1) / 2:
            if myStr[i] != myStr[j]:
                return False
            j = j - 1
            i = i + 1
        return True
