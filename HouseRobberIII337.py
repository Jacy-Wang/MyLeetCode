# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        return max(res)

    def helper(self, root):
        if not root:
            return (0, 0)
        left = self.helper(root.left)
        right = self.helper(root.right)
        res1 = root.val + left[1] + right[1]
        res2 = max(left) + max(right)
        return (res1, res2)
