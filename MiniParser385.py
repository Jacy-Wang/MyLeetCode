# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0].isdigit() or s[0] == '-':
            return NestedInteger(int(s))
        res = NestedInteger()
        stack = []
        num = ""
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c.isdigit() or c == '-':
                num += c
            elif c == ',' or c == ']':
                if num:
                    top = stack.pop()
                    top.add(int(num))
                    stack.append(top)
                    num = ""
                if c == ']':
                    top = stack.pop()
                    if stack:
                        prev = stack.pop()
                        prev.add(top)
                        stack.append(prev)
                    else:
                        return top
