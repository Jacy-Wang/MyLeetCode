# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        return self.getSum(root, 0)

    def getSum(self, root, curSum):
        if not root:
            return False
        curSum = curSum + root.val
        if not root.left and not root.right:
            if curSum == self.sum:
                return True
            else:
                return False
        else:
            return self.getSum(root.left, curSum) or self.getSum(root.right, curSum)
