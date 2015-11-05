tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.cand = []
            self.find(0, root)
            return max(self.cand)
        else:
            return 0

    def find(self, length, node):
        if node.left:
            self.cand.append(self.find(length + 1, node.left))
        if node.right:
            self.cand.append(self.find(length + 1, node.right))
        self.cand.append(length + 1)
