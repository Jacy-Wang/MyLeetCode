# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.nums = []
        self.findPaths(root, "")
        return reduce(lambda x, y : int(x) + int(y), self.nums, 0)
        
    def findPaths(self, root, curStr):
        if not root.left and not root.right:
            self.nums.append(curStr + str(root.val))
        if root.left:
            self.findPaths(root.left, curStr + str(root.val))
        if root.right:
            self.findPaths(root.right, curStr + str(root.val))
