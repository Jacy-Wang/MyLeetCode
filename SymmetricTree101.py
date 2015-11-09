# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.decide(root.left, root.right)
        return True
    
    def decide(self, a, b):
        if not a and not b:
            return True
        elif not a or not b:
            return False
        elif a.val == b.val:
            return self.decide(a.left, b.right) and self.decide(a.right, b.left)
        return False
