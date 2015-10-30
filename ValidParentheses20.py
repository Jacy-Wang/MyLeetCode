class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        myDict = {'(' : ')', '[' : ']', '{' : '}', ')' : 'a', ']' : 'b', '}' : 'c'}
        stack.append(s[0])
        for i in xrange(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] == myDict[stack[len(stack) - 1]]:
                stack.pop()
            else:
                stack.append(s[i])

        return True if len(stack) == 0 else False
