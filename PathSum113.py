# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.sum = sum
        self.paths = []
        self.findPath(root, 0, [])
        return self.paths
        
    def findPath(self, root, curSum, curPaths):
        curSum += root.val
        curPaths.append(root.val)
        if not root.left and not root.right:
            if curSum == self.sum:
                self.paths.append(copy.deepcopy(curPaths))
        if root.left:
            self.findPath(root.left, curSum, curPaths)
        if root.right:
            self.findPath(root.right, curSum, curPaths)
        length = len(curPaths)
        curPaths[:] = curPaths[: length - 1]
