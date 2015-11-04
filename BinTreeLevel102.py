tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = Queue.Queue()
        q.put_nowait((0, root))
        res = []
        level = -1
        while not q.empty():
            item = q.get_nowait()
            if item[0] == level + 1:
                if level > -1:
                    res.append(levelRes)
                level = level + 1
                levelRes = [item[1].val]
            else:
                levelRes.append(item[1].val)
            if item[1].left:
                q.put_nowait((level + 1, item[1].left))
            if item[1].right:
                q.put_nowait((level + 1, item[1].right))
        res.append(levelRes)
        return res
