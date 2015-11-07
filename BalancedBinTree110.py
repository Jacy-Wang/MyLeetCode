# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.check(root) == -1:
            return False
        return True

    def check(self, node):
        if not node:
            return 0
        leftLength = self.check(node.left)
        if leftLength == -1:
            return -1
        rightLength = self.check(node.right)
        if rightLength == -1:
            return -1
        if abs(leftLength - rightLength) > 1:
            return -1
        return max(leftLength, rightLength) + 1
