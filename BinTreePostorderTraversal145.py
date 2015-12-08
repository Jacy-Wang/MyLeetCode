# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        lastVisited = None
        res = []
        stack = []
        stack.append(root)
        while stack:
            top = stack.pop()
            if top.right:
                if lastVisited == top.right:
                    res.append(top.val)
                    lastVisited = top
                else:
                    stack.append(top)
                    stack.append(top.right)
                    if top.left:
                        stack.append(top.left)
            elif top.left:
                if lastVisited == top.left:
                    res.append(top.val)
                    lastVisited = top
                else:
                    stack.append(top)
                    stack.append(top.left)
            else:
                res.append(top.val)
                lastVisited = top
        return res
