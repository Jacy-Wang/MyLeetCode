class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            return (self.findKth(nums1, nums2, n / 2 - 1) + self.findKth(nums1, nums2, n / 2)) / 2.0
        else:
            return self.findKth(nums1, nums2, n / 2)
            
    def findKth(self, arr1, arr2, k):
        """k is index, starting from 0"""
        if not arr1:
            return arr2[k]
        if not arr2:
            return arr1[k]
        len1 = len(arr1)
        len2 = len(arr2)
        if len1 / 2 + len2 / 2 >= k:
            if arr1[len1 / 2] >= arr2[len2 / 2]:
                return self.findKth(arr1[: len1 / 2], arr2, k)
            else:
                return self.findKth(arr1, arr2[: len2 / 2], k)
        else:
            if arr1[len1 / 2] >= arr2[len2 / 2]:
                return self.findKth(arr1, arr2[len2 / 2 + 1 :], k - len2 / 2 - 1)
            else:
                return self.findKth(arr1[len1 / 2 + 1 :], arr2, k - len1 / 2 - 1)
