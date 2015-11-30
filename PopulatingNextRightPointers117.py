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
            firstNode = root
            while firstNode:
                curNode = firstNode
                firstNode = None
                prevNode = None
                while curNode:
                    if not firstNode:
                        if curNode.left:
                            firstNode = curNode.left
                        elif curNode.right:
                            firstNode = curNode.right
                    if curNode.left:
                        if prevNode:
                            prevNode.next = curNode.left
                        prevNode = curNode.left
                    if curNode.right:
                        if prevNode:
                            prevNode.next = curNode.right
                        prevNode = curNode.right
                    curNode = curNode.next
