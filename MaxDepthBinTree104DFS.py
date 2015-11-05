# Definition for a binary tree node.
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
            maxLength = 0
            stack = []
            stack.append((root, 1))
            while stack:
                top = stack.pop()
                if top[0].left:
                    stack.append((top[0].left, top[1] + 1))
                if top[0].right:
                    stack.append((top[0].right, top[1] + 1))
                maxLength = max(maxLength, top[1])
            return maxLength
        else:
            return 0
