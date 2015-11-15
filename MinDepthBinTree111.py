# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = Queue.Queue()
        queue.put_nowait((root, 1))
        while not queue.empty():
            top = queue.get_nowait()
            if not top[0].left and not top[0].right:
                return top[1]
            if top[0].left:
                queue.put_nowait((top[0].left, top[1] + 1))
            if top[0].right:
                queue.put_nowait((top[0].right, top[1] + 1))
