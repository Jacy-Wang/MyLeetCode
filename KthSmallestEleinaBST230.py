# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.stack = []
        self.goLeft(root)
        counter = 0
        while self.stack and counter < k:
            top = self.stack.pop()
            counter += 1
            if top.right:
                self.goLeft(top.right)
        return top.val

    def goLeft(self, root):
        p = root
        while p:
            self.stack.append(p)
            p = p.left
