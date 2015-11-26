# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.stack = []
        val = []
        node = root
        self.goLeftmost(node)
        while self.stack:
            top = self.stack.pop()
            val.append(top.val)
            node = top.right
            self.goLeftmost(node)
        return val

    def goLeftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left
