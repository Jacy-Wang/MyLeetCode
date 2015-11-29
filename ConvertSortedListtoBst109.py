# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        self.nums = nums
        return self.gen(0, len(nums) - 1)
        
    def gen(self, left, right):
        if left > right:
            return None
        elif left == right:
            return TreeNode(self.nums[left])
        else:
            mid = (left + right) / 2
            leftTree = self.gen(left, mid - 1)
            rightTree = self.gen(mid + 1, right)
            root = TreeNode(self.nums[mid])
            root.left = leftTree
            root.right = rightTree
            return root
