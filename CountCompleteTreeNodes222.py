# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        p = root.left
        self.level = 0
        while p:
            self.level += 1
            p = p.left
        self.num = 2 ** (self.level) - 1
        self.binarySearch(root, 0)
        return self.num
        
    def binarySearch(self, root, level):
        if level == self.level:
            self.num += 1
        else:
            if not root.right:
                self.num += 1
            else:
                p = root.right
                curLevel = level + 1
                while p.left:
                    p = p.left
                    curLevel += 1
                if curLevel < self.level:
                    self.binarySearch(root.left, level + 1)
                else:
                    self.num += 2 ** (self.level - level - 1)
                    self.binarySearch(root.right, level + 1)
