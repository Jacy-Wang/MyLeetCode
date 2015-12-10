# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = []
        q2 = []
        if not root:
            return res
        q.append(root)
        while 1:
            rightEle = root.val
            while q:
                top = q.pop(0)
                if top.left:
                    q2.append(top.left)
                if top.right:
                    q2.append(top.right)
                rightEle = top.val
            res.append(rightEle)
            q = q2
            q2 = []
            if not q:
                return res
