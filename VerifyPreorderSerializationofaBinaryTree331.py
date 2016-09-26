class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for v in preorder.split(","):
            stack.append(v)
            while len(stack) >= 3 and stack[-2 :] == ["#"] * 2 and stack[-3] != "#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack[0] == "#"
