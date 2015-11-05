# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        #print root.val, type(root.val)
        self.res = []
        self.find("", root)
        for i in xrange(len(self.res)):
            self.res[i] = self.res[i][2 :]
        return self.res

    def find(self, path, node):
        if not node.left and not node.right:
            self.res.append(path + "->" + str(node.val))
        if node.left:
            self.find(path + "->" + str(node.val), node.left)
        if node.right:
            self.find(path + "->" + str(node.val), node.right)
