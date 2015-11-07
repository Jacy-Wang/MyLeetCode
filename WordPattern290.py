class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern == str == "":
            return False
        myStr = str.split(" ")
        if len(myStr) != len(pattern):
            return False
        myDict = {}
        for i in xrange(len(pattern)):
            if pattern[i] not in myDict.keys():
                for v in myDict.keys():
                    if myDict[v] == myStr[i]:
                        return False
                myDict[pattern[i]] = myStr[i]
            else:
                if myDict[pattern[i]] != myStr[i]:
                    return False
        return True
