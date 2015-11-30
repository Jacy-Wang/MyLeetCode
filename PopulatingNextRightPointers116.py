# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            node = root
            while node:
                curNode = node
                if node.left:
                    while curNode.next:
                        curNode.left.next = curNode.right
                        curNode.right.next = curNode.next.left
                        curNode = curNode.next
                    curNode.left.next = curNode.right
                    node = node.left
                else:
                    break
