# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.gen(1, n)
    
    def gen(self, left, right):
        res = []
        if left > right:
            res.append(None)
            return res
        else:
            for i in xrange(left, right + 1):
                leftTrees = self.gen(left, i - 1)
                rightTrees = self.gen(i + 1, right)
                for j in xrange(len(leftTrees)):
                    for k in xrange(len(rightTrees)):
                        curRoot = TreeNode(i)
                        curRoot.left = leftTrees[j]
                        curRoot.right = rightTrees[k]
                        res.append(curRoot)
            return res
