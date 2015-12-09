# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        if root:
            self.lst = []
            self.traverse(root)
            self.index = 0
        
    def traverse(self, root):
        if root.left:
            self.traverse(root.left)
        self.lst.append(root.val)
        if root.right:
            self.traverse(root.right)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.root:
            return self.index < len(self.lst)
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.lst[self.index - 1]
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
