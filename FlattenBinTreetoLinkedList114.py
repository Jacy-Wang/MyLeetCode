# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            right = root.right
            rightMost = root
            node = root
            sign = False
            while node.left:
                curNode = node.left
                while curNode.right:
                    curNode = curNode.right
                    sign = True
                rightMost = curNode
                if sign:
                    break
                node = node.left
            if root.left:
                root.right = root.left
                root.left = None
            rightMost.right = right
            root = root.right
